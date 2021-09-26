# pylint:disable=C0111,C0103

def get_average_purchase(db):
    '''return the average amount spent per order for each customer ordered by customer ID'''
    request = '''
        WITH OrderValues AS (
          SELECT SUM(od.UnitPrice * od.Quantity) AS value, od.OrderID
          FROM OrderDetails od
          GROUP BY od.OrderID
        )
        SELECT ROUND(AVG(ov.value), 2) AS average, c.CustomerID
        FROM Customers c
        JOIN Orders o ON c.CustomerID = o.CustomerID
        JOIN OrderValues ov ON ov.OrderID = o.OrderID
        GROUP BY c.CustomerID
        ORDER BY c.CustomerID
    '''
    return db.execute(request).fetchall()

def get_general_avg_order(db):
    '''return the average amount spent per order'''
    request = '''
        WITH OrderValues AS (
          SELECT SUM(od.Quantity * od.UnitPrice) AS value
          FROM OrderDetails od
          GROUP BY od.OrderID
        )
        SELECT ROUND(AVG(ov.value), 2)
        FROM OrderValues ov
    '''
    return db.execute(request).fetchone()[0]


def display_best_buyers(db):
    '''return the customers who have an average purchase bigger than the
    general average purchase'''
    # It shoud return a list of tuple (average, customer_id) ordered by customer ID
    request = '''
        WITH OrderValues AS (
          SELECT SUM(od.UnitPrice * od.Quantity) AS value, od.OrderID
          FROM OrderDetails od
          GROUP BY od.OrderID
        ), GeneralOrderValue AS (
          SELECT ROUND(AVG(ov.value), 2) AS average FROM OrderValues ov
        ), CustomerOrderValue AS (
          SELECT ROUND(AVG(ov.value), 2) AS average, c.CustomerID
          FROM Customers c
          JOIN Orders o ON c.CustomerID = o.CustomerID
          JOIN OrderValues ov ON ov.OrderID = o.OrderID
          GROUP BY c.CustomerID
          ORDER BY c.CustomerID
        )
        SELECT CustomerOrderValue.average, CustomerOrderValue.CustomerID
        FROM CustomerOrderValue
        WHERE CustomerOrderValue.average > (SELECT average FROM GeneralOrderValue)
    '''
    return db.execute(request).fetchall()
