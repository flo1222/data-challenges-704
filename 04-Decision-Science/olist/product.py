import pandas as pd
import numpy as np
from olist.data import Olist
from olist.order import Order


class Product:

    def __init__(self):
        # Import only data once
        olist = Olist()
        self.data = olist.get_data()
        self.matching_table = olist.get_matching_table()
        self.order = Order()

    def get_product_features(self):
        """
        Returns a DataFrame with:
       'product_id', 'product_category_name', 'product_name_length',
       'product_description_length', 'product_photos_qty', 'product_weight_g',
       'product_length_cm', 'product_height_cm', 'product_width_cm'
        """

        products = self.data['products']

        # (optional) convert name to english
        en_category = self.data['product_category_name_translation']
        df = products.merge(en_category, on='product_category_name')
        df.drop(['product_category_name'], axis=1, inplace=True)
        df.rename(columns={'product_category_name_english': 'category'},
                  inplace=True)


        return df

    def get_price(self):
        """
        Return a DataFrame with:
        'product_id', 'price'
        """

        products = self.data['products']
        order_items = self.data['order_items']
        return products[['product_id']].merge(order_items[['product_id', 'price']], on='product_id')

    def get_wait_time(self):
        """
        Returns a DataFrame with:
        'product_id', 'wait_time'
        """
        matching_table = self.matching_table
        orders_wait_time = self.order.get_wait_time()

        df = matching_table.merge(orders_wait_time,
                                 on='order_id')

        return df.groupby('product_id',
                          as_index=False).agg({'wait_time': 'mean'})

    def get_review_score(self):
        """
        Returns a DataFrame with:
        'product_id', 'share_of_five_stars', 'share_of_one_stars',
        'review_score'
        """
        matching_table = self.matching_table
        orders_reviews = self.order.get_review_score()

        # Since same products can appear multiple times in the same
        # order, create a product <> order matching table

        matching_table = matching_table[['order_id',
                                         'product_id']].drop_duplicates()
        df = matching_table.merge(orders_reviews,
                                  on='order_id')
        def cost(x):
            cost = 0
            for score in x:
                if score == 1:
                    cost +=50
                if score == 2:
                    cost += 25
                if score == 3:
                    cost += 20
            return cost

        df = df.groupby('product_id',
                        as_index=False).agg({'dim_is_one_star': 'mean',
                                             'dim_is_five_star': 'mean',
                                             'review_score': ['mean', cost]})
        df.columns = ['product_id', 'share_of_one_stars',
                      'share_of_five_stars', 'review_score', 'review_cost']

        return df

    def get_quantity(self):
        """
        Returns a DataFrame with:
        'product_id', 'n_orders', 'quantity'
        """
        matching_table = self.matching_table
        order_items = self.data['order_items']
        tmp = matching_table.merge(order_items[['product_id', 'price']], on='product_id')
        n_orders =\
            matching_table.groupby('product_id')['order_id'].nunique().reset_index()
        n_orders.columns = ['product_id', 'n_orders']

        quantity = \
            matching_table.groupby('product_id',
                                   as_index=False).agg({
                                       'order_id': 'count'
                                       })
        quantity.columns = ['product_id', 'quantity']
        
        mean_price= \
            tmp.groupby('product_id',
                                   as_index=False).agg({
                                       'price':'mean'
                                       })
        mean_price.columns = ['product_id', 'mean_price']
        order_qty = n_orders.merge(quantity, on='product_id')
        return order_qty.merge(mean_price, on='product_id')

    def get_training_data(self):

        training_set =\
            self.get_product_features()\
                .merge(
                self.get_wait_time(), on='product_id'
               ).merge(
                self.get_review_score(), on='product_id'
               ).merge(
                self.get_quantity(), on='product_id'
               )

        return training_set

    def get_product_cat(self, agg="median"):
        '''
        Returns a DataFrame aggregating various properties for each product 'category',
        using the aggregation function passed in argument.
        The 'quantity' columns refers to the total number of product sold for this category.
        '''
        product_cat = self.get_training_data().groupby("category").agg(
            {
                "review_score": agg,
                "share_of_one_stars": agg,
                "share_of_five_stars": agg,
                "wait_time": agg,
                "price": agg,
                "product_weight_g": agg,
                "product_length_cm": agg,
                "product_height_cm": agg,
                "product_width_cm": agg,
                "product_photos_qty": agg,
                "n_orders": agg,
                "quantity": "sum",
            }
        )
        return product_cat



# Below is a version of the code in pure SQL

# import pandas as pd
# import pandasql as ps
# import numpy as np
# from olist.data import Olist
# from olist.order import Order
# ​
# ​
# class Product:
# ​
#     def __init__(self):
#         # Import only data once
#         olist = Olist()
#         self.data = olist.data_dict
#         self.matching_table = olist.get_matching_table()
#         self.order = Order()
# ​
#     def get_training_data(self):
# ​
#         data = self.data
#         orders = data['orders']
#         products = data['products']
#         customers = data['customers']
#         reviews = data['order_reviews']
#         order_item = data['order_items']
#         geoloc = data['geolocation']
#         payment = data['order_payments']
#         sellers = data['sellers']
#         cat_name = data['product_category_name_translation']
# ​
#         q1 = """
#             SELECT
#             p.product_id,
#             t.product_category_name_english AS category,
#             p.product_photos_qty,
#             p.product_weight_g AS weight,
#             p.product_length_cm AS length,
#             p.product_height_cm AS height,
#             p.product_width_cm AS withd,
#             AVG(oi.freight_value) AS avg_freight_value,
#             p.product_name_length,
#             p.product_description_length,
#             COUNT(DISTINCT o.order_id) AS n_order,
#             COUNT(oi.order_id) AS quantity,
#             AVG(julianday(o.order_delivered_customer_date) - julianday(o.order_purchase_timestamp)) AS wait_time,
#             COUNT(DISTINCT CASE WHEN r.review_score = 5 THEN o.order_id END) AS share_of_five_stars,
#             COUNT(DISTINCT CASE WHEN r.review_score = 1 THEN o.order_id END) AS share_of_one_stars,
#             AVG(r.review_score) AS review_score
#             FROM orders as o
#             INNER JOIN order_item AS oi ON oi.order_id = o.order_id
#             INNER JOIN products AS p ON p.product_id = oi.product_id
#             INNER JOIN cat_name AS t ON t.product_category_name = p.product_category_name
#             INNER JOIN reviews AS r on r.order_id = o.order_id
#             GROUP BY 1,2,3,4,5,6,7,9,10
#             ORDER BY 11 DESC
#         """
# ​
#         product_df = ps.sqldf(q1)
#         return product_df
