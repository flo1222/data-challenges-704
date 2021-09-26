import pandas as pd
import numpy as np
from olist.data import Olist
from olist.order import Order


class Seller:

    def __init__(self):
        # Import only data once
        olist = Olist()
        self.data = olist.get_data()
        self.matching_table = olist.get_matching_table()
        self.order = Order()

    def get_seller_features(self):
        """
        Returns a DataFrame with:
        'seller_id', 'seller_city', 'seller_state'
        """
        sellers = self.data['sellers']
        sellers.drop('seller_zip_code_prefix',
                     axis=1,
                     inplace=True)
        # There is multiple rows per seller
        sellers.drop_duplicates(inplace=True)

        return sellers

    def get_seller_delay_wait_time(self):
        """
        Returns a DataFrame with:
        'seller_id', 'delay_to_carrier', 'wait_time'
        """
        # Get data
        order_items = self.data['order_items']
        orders = self.data['orders'].query("order_status=='delivered'")

        ship = order_items.merge(orders, on='order_id')

        # Handle datetime
        ship.loc[:, 'shipping_limit_date'] =\
            pd.to_datetime(ship['shipping_limit_date'])
        ship.loc[:, 'order_delivered_carrier_date'] =\
            pd.to_datetime(ship['order_delivered_carrier_date'])
        ship.loc[:, 'order_delivered_customer_date'] =\
            pd.to_datetime(ship['order_delivered_customer_date'])
        ship.loc[:, 'order_purchase_timestamp'] =\
            pd.to_datetime(ship['order_purchase_timestamp'])

        # Compute delay and wait_time
        def delay_to_logistic_partner(d):
            days = np.mean(
                (d.shipping_limit_date - d.order_delivered_carrier_date)/np.timedelta64(24, 'h')
                )
            if days < 0:
                return abs(days)
            else:
                return 0

        def order_wait_time(d):
            days = np.mean(
                (d.order_delivered_customer_date - d.order_purchase_timestamp)/np.timedelta64(24, 'h')
                )
            return days

        delay = ship.groupby('seller_id')\
                    .apply(delay_to_logistic_partner)\
                    .reset_index()
        delay.columns = ['seller_id', 'delay_to_carrier']

        wait = ship.groupby('seller_id')\
                   .apply(order_wait_time)\
                   .reset_index()
        wait.columns = ['seller_id', 'wait_time']

        df = delay.merge(wait, on='seller_id')

        return df

    def get_active_dates(self):
        orders = self.data['orders'][['order_id', 'order_approved_at']].copy()

        # create two new columns in view of aggregating
        orders.loc[:,'date_first_sale'] = pd.to_datetime(orders['order_approved_at'])
        orders['date_last_sale'] = orders['date_first_sale']

        return orders.merge(self.matching_table[['seller_id', 'order_id']], on="order_id")\
            .groupby('seller_id')\
            .agg({
            "date_first_sale": min,
            "date_last_sale": max
        })

    def get_review_score(self):
        """
        Returns a DataFrame with:
        'seller_id', 'share_of_five_stars', 'share_of_one_stars', 'review_score'
        """
        matching_table = self.matching_table
        orders_reviews = self.order.get_review_score()

        # Since same seller can appear multiple times in the same
        # order, create a seller <> order matching table

        matching_table = matching_table[['order_id',
                                         'seller_id']].drop_duplicates()
        df = matching_table.merge(orders_reviews,
                                  on='order_id')

        df = df.groupby('seller_id',
                        as_index=False).agg({'dim_is_one_star': 'mean',
                                             'dim_is_five_star': 'mean',
                                             'review_score': 'mean'})
        df.columns = ['seller_id', 'share_one_stars',
                      'share_of_five_stars', 'review_score']

        return df

    def get_quantity(self):
        """
        Returns a DataFrame with:
        'seller_id', 'n_orders', 'quantity'
        """
        matching_table = self.matching_table

        n_orders = matching_table.groupby('seller_id')['order_id']\
            .nunique()\
            .reset_index()
        n_orders.columns = ['seller_id', 'n_orders']

        quantity = matching_table.groupby('seller_id', as_index=False).agg({'order_id': 'count'})
        quantity.columns = ['seller_id', 'quantity']

        return n_orders.merge(quantity, on='seller_id')

    def get_sales(self):
        """
        Returns a DataFrame with:
        'seller_id', 'sales'
        """
        return self.data['order_items'][['seller_id', 'price']]\
            .groupby('seller_id')\
            .sum()\
            .rename(columns={'price': 'sales'})


    def get_training_data(self):

        training_set =\
            self.get_seller_features()\
                .merge(
                self.get_seller_delay_wait_time(), on='seller_id'
               ).merge(
                self.get_active_dates(), on='seller_id'
               ).merge(
                self.get_review_score(), on='seller_id'
               ).merge(
                self.get_quantity(), on='seller_id'
               ).merge(
                self.get_sales(), on='seller_id'
               )

        return training_set

#My initial code


# import pandas as pd
# import numpy as np
# from olist.data import Olist
# from olist.order import Order


# class Seller:

#     def __init__(self):
#         # Import only data once
#         olist = Olist()
#         self.data = olist.get_data()
#         self.matching_table = olist.get_matching_table()
#         self.order = Order()

#     def get_seller_features(self):
#         """
#         Returns a DataFrame with:
#        'seller_id', 'seller_city', 'seller_state'
#         """
#         return self.data["sellers"][["seller_id","seller_city","seller_state"]]

#     def get_seller_delay_wait_time(self):
#         """
#         Returns a DataFrame with:
#        'seller_id', 'delay_to_carrier', 'seller_wait_time'
#         """
#         orders = self.data["orders"].copy()
#         orders = orders.query("order_status=='delivered'").copy()
#         orders.loc[:, 'order_delivered_carrier_date'] = \
#             pd.to_datetime(orders['order_delivered_carrier_date'])
#         orders.loc[:, 'order_purchase_timestamp'] = \
#             pd.to_datetime(orders['order_purchase_timestamp'])
#         #Creating delay to carrier
#         orders.loc[:, 'delay_to_carrier'] =(orders['order_delivered_carrier_date'] -\
#              orders['order_purchase_timestamp']) / np.timedelta64(24, 'h')    
        
#         #Build dataframe
#         seller_delay = self.matching_table.merge(Order().get_wait_time(), on = "order_id")\
#                 .merge(orders, on = 'order_id')[["seller_id", "wait_time", "delay_to_carrier"]]

#         #Aggregate on seller_id
#         seller_delay = seller_delay.groupby("seller_id", as_index=False)\
#             .agg({'wait_time': 'mean', 'delay_to_carrier':'mean'})

#         return seller_delay
        
#     def get_active_dates(self):
#         """
#         Returns a DataFrame with:
#        'seller_id', 'date_first_sale', 'date_last_sale'
#         """
#         orders = self.data["orders"].copy()
#         orders = orders.query("order_status=='delivered'").copy()
        
#         #build initial dataframe
#         tmp = orders.merge(self.matching_table, on = 'order_id')[["order_purchase_timestamp", "seller_id"]]

#         #Get first and last date, then merge
#         first = tmp.sort_values(by = "order_purchase_timestamp")\
#                 .groupby("seller_id", as_index = False).first().rename(columns = {'order_purchase_timestamp' : 'date_first_sale'})
#         last = tmp.sort_values(by = "order_purchase_timestamp", ascending = False)\
#                 .groupby("seller_id", as_index = False).first().rename(columns = {'order_purchase_timestamp' : 'date_last_sale'})
#         return first.merge(last, on = "seller_id")
        
#     def get_review_score(self):
#         """
#         Returns a DataFrame with:
#         'seller_id', 'share_of_five_stars', 'share_of_one_stars',
#         'review_score'
#         """
#         reviews = self.order.get_review_score()
#         #Build base dataframe
#         reviews_df = reviews.merge(self.matching_table, on = "order_id")\
#             [["seller_id", "dim_is_five_star", "dim_is_one_star", "review_score", "order_id"]]
#         #Aggregate for the required stats
#         review_stats = reviews_df.groupby("seller_id", as_index = False).agg({\
#                              "dim_is_five_star":"sum",
#                              "dim_is_one_star":"sum",
#                              "review_score":"mean",
#                              "order_id": "count"            
#                              })
#         #Build columns with the shares
#         review_stats.loc[:, 'share_of_five_stars'] = review_stats["dim_is_five_star"]/review_stats["order_id"]
#         review_stats.loc[:, 'share_of_one_stars'] = review_stats["dim_is_one_star"]/review_stats["order_id"]
        
#         return review_stats[['seller_id', 'share_of_five_stars', 'share_of_one_stars', 'review_score']]


#     def get_quantity(self):
#         """
#         Returns a DataFrame with:
#         'seller_id', 'n_orders', 'quantity', 'quantity_per_order'
#         """
#         #Get the required counts from the matching table
#         seller_quantity = self.matching_table.groupby("seller_id", as_index = False).agg({\
#                                                     'order_id':'nunique',
#                                                     'product_id':'count' 
#                                             }).rename(columns = {'order_id':'n_orders', 'product_id':'quantity'})
#         #Compute the quantity per order
#         seller_quantity.loc[:, 'quantity_per_order'] = seller_quantity["quantity"]/seller_quantity["n_orders"]
#         return seller_quantity

#     def get_sales(self):
#         """
#         Returns a DataFrame with:
#         'seller_id', 'sales'
#         """
#         all_sales = self.matching_table.merge(Order().get_price_and_freight(), on = "order_id")
#         seller_sales = all_sales.groupby("seller_id", as_index = False).agg({
#             'price':'sum'
#         }).rename(columns={'price':'sales'}) 
#         return seller_sales

#     def get_training_data(self):
#         """
#         Returns a DataFrame with:
#         'seller_id', 'seller_state', 'seller_city', 'delay_to_carrier',
#         'seller_wait_time', 'share_of_five_stars', 'share_of_one_stars',
#         'seller_review_score', 'n_orders', 'quantity', 'date_first_sale', 'date_last_sale', 'sales'
#         """
#         df = self.get_seller_features()\
#             .merge(self.get_seller_delay_wait_time(), on = 'seller_id')\
#             .merge(self.get_review_score(), on = 'seller_id')\
#             .merge(self.get_active_dates(), on = 'seller_id')\
#             .merge(self.get_quantity(), on = 'seller_id')\
#             .merge(self.get_sales(), on = 'seller_id')
#         df = df.rename(columns={'wait_time':'seller_wait_time','review_score':'seller_review_score'})
#         return df