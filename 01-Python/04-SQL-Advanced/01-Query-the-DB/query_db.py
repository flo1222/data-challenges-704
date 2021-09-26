# pylint:disable=C0111,C0103

def query_orders(db):
    """return a list of orders with displaying each column"""
    request = '''
        select * 
        from Orders o 
        order by o.OrderID asc
    '''
    db.execute(request)
    results = db.fetchall()
    return results


def get_orders_range(db, date_from, date_to):
    """return a list of orders with all columns with OrderDate between
    date_from to date_to"""
    request = '''
        select * 
        from Orders o 
        where o.OrderDate > ? and o.OrderDate <= ?
    '''
    db.execute(request, (date_from,date_to))
    results = db.fetchall()
    return results


def get_waiting_time(db):
    """get a list with all the orders with each column + and calculate an extra
    TimeDelta column displaying the number of days between OrderDate and
    ShippedDate ordered by ascending timedelta"""
    request = '''
        SELECT *, 
        julianday(ShippedDate) - julianday(OrderDate) as delay
        from Orders o 
        order by delay
    '''
    db.execute(request)
    results = db.fetchall()
    return results

# To test your code, you can **run it** before running `make`
#   => Uncomment the following lines + run:
#   $ python school.py
# import sqlite3
# conn = sqlite3.connect('db/ecommerce.sqlite')
# db = conn.cursor()
# print(get_waiting_time(db))
