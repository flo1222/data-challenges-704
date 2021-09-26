# pylint: disable-all

import unittest
from bs4 import BeautifulSoup


class Users(unittest.TestCase):
    # 1 in the good folders

    # 2 should have a customers table
    def test_customers_table_exists(self):
        with open('ecommerce.xml', 'r') as file:
            data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        tables = soup.find_all('table')
        t = []
        for table in tables:
            t.append(table['name'])
        self.assertEqual('customers' in t, True)

    # 2' customers should have the correct fields
    def test_customers_should_have_the_correct_fields(self):
        with open('ecommerce.xml', 'r') as file:
            data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        table = soup.find_all('table', attrs={"name": "customers"})
        fields = [row.get('name') for row in table[0].find_all('row')]
        correct_fields = ['first_name', 'last_name', 'email', 'city', 'id']
        fields.sort()
        correct_fields.sort()
        self.assertEqual(fields, correct_fields)

    # 3 should have a products table
    def test_products_table_exists(self):
        with open('ecommerce.xml', 'r') as file:
            data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        tables = soup.find_all('table')
        t = []
        for table in tables:
            t.append(table['name'])
        self.assertEqual('products' in t, True)

    # 3' products should have the correct fields
    def test_products_should_have_the_correct_fields(self):
        with open('ecommerce.xml', 'r') as file:
            data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        table = soup.find_all('table', attrs={"name": "products"})
        fields = [row.get('name') for row in table[0].find_all('row')]
        correct_fields = ['name', 'unit_price', 'id']
        fields.sort()
        correct_fields.sort()
        self.assertEqual(fields, correct_fields)

    # 4 should have an orders table
    def test_orders_table_exists(self):
        with open('ecommerce.xml', 'r') as file:
            data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        tables = soup.find_all('table')
        t = []
        for table in tables:
            t.append(table['name'])
        self.assertEqual('orders' in t, True)

    # 4' should have customer_id, foreign_key
    def test_orders_should_have_the_correct_fields(self):
        with open('ecommerce.xml', 'r') as file:
            data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        table = soup.find_all('table', attrs={"name": "orders"})
        fields = [row.get('name') for row in table[0].find_all('row')]
        correct_fields = ['date_of_order', 'customer_id', 'id']
        fields.sort()
        correct_fields.sort()
        self.assertEqual(fields, correct_fields)

    # 5 should have a product_orders table
    def test_product_orders_table_exists(self):
        with open('ecommerce.xml', 'r') as file:
            data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        tables = soup.find_all('table')
        t = []
        for table in tables:
            t.append(table['name'])
        self.assertEqual('product_orders' in t, True)

    # 5' product_orders should have the correct fields
    def test_product_orders_should_have_the_correct_fields(self):
        with open('ecommerce.xml', 'r') as file:
            data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        table = soup.find_all('table', attrs={"name": "product_orders"})
        fields = [row.get('name') for row in table[0].find_all('row')]
        correct_fields = ['product_id', 'order_id', 'quantity', 'id']
        fields.sort()
        correct_fields.sort()
        self.assertEqual(fields, correct_fields)
