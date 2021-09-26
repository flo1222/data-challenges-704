# pylint:disable=C0111,C0103

def detailed_orders(db):
    '''return the list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''
    request = '''
        select OrderID , c.ContactName, e.FirstName  
        from Orders o 
        Join Employees e on o.EmployeeId = e.EmployeeId
        Join customers c on o.CustomerId = c.CustomerId
        order by o.OrderID 
    '''
    db.execute(request)
    results = db.fetchall()
    return results


def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
    amount (keep only 2 numbers after the ',')
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''
    request = '''
        select 
            c.ContactName,  
            ROUND(SUM(od.UnitPrice * od.Quantity),1) as spent_total
        from Orders o 
        Join customers c on o.CustomerId = c.CustomerId
        join OrderDetails od on o.OrderID = od.OrderID 
        GROUP by o.CustomerID 
        ORDER by spent_total
    '''
    db.execute(request)
    results = db.fetchall()
    return results


def best_employee(db):
    '''return the first and last name of the best employee (the one who sell
    the most in terms of amount of money'''
    request = '''
        select 
            e.FirstName , 
            e.LastName Name , 
            ROUND(SUM(od.UnitPrice * od.Quantity),1) as sold_total
        from Orders o 
        Join Employees e on o.EmployeeID = e.EmployeeID 
        join OrderDetails od on o.OrderID = od.OrderID 
        GROUP by e.EmployeeID 
        order by sold_total desc
    '''
    db.execute(request)
    results = [db.fetchone()]
    return results


def orders_per_customer(db):
    '''return a list of tuple where each tupe contains the contactName of the
    customer and the number of orders he made (contactName, number_of_orders).
    Order the list by ascending number of orders'''
    request = '''
        select 
            c.ContactName, 
            count(o.OrderID) as order_count
        from Customers c 
        left join Orders o on o.CustomerID = c.CustomerID 
        group by c.CustomerID 
        order by order_count
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
# print(orders_per_customer(db))
