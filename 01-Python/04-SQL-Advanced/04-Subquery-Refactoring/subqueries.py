# pylint:disable=C0111,C0103

def get_average_purchase(db):
    '''return the average amount spent per order for each customer ordered by customer ID'''
    request = '''
        select
            ROUND(AVG(order_spent),2),
            CustomerID
        from(
            select 
                c.ContactName,
                c.CustomerID, 
                od.OrderDetailID, 
                SUM(od.UnitPrice * od.Quantity) as order_spent
            from Orders o 
            Join customers c on o.CustomerId = c.CustomerId
            join OrderDetails od on o.OrderID = od.OrderID
            group by o.OrderID 
        )
        group by ContactName
        order by CustomerID
    '''
    db.execute(request)
    results = db.fetchall()
    return results



def get_general_avg_order(db):
    '''return the average amount spent per order'''
    request = '''
        select ROUND(AVG(order_spent),2)
        from(
            select 
                o.OrderID ,
                c.ContactName,
                c.CustomerID, 
                SUM(od.UnitPrice * od.Quantity) as order_spent
            from Orders o 
            Join Customers c  on c.CustomerID = o.CustomerID 
            join OrderDetails od on o.OrderID = od.OrderID
            group by o.OrderID 
        )
    '''
    db.execute(request)
    results = db.fetchone()
    return results[0]


def display_best_buyers(db):
    '''return the customers who have an average purchase bigger than the
    general average purchase'''
    # It shoud return a list of tuple (average, customer_id) ordered by customer ID
    request = '''
        with test AS (
            select
                CustomerID, 
                ROUND(AVG(order_spent),2) as avg_cust
            from(
                select 
                    c.ContactName,
                    c.CustomerID, 
                    od.OrderDetailID, 
                    SUM(od.UnitPrice * od.Quantity) as order_spent
                from Orders o 
                Join customers c on o.CustomerId = c.CustomerId
                join OrderDetails od on o.OrderID = od.OrderID
                group by o.OrderID 
            )
            group by ContactName
            order by CustomerID
        )
        select avg_cust, CustomerID from test where avg_cust > ?
    '''
    db.execute(request, (get_general_avg_order(db),))
    results = db.fetchall()
    return results

# To test your code, you can **run it** before running `make`
#   => Uncomment the following lines + run:
# #   $ python school.py
# import sqlite3
# conn = sqlite3.connect('db/ecommerce.db')
# db = conn.cursor()
# print(display_best_buyers(db))
