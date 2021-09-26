# pylint: disable-all

import unittest
from bs4 import BeautifulSoup

class Users(unittest.TestCase):

    def test_customers_table_exists(self):
        with open('customers.xml', 'r') as file:
          data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        self.assertEqual(soup.table['name'],'customers')

    def test_should_only_have_users_table(self):
        with open('customers.xml', 'r') as file:
          data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        self.assertEqual(len(soup.find_all("table", attrs={"name": "customers"})), 1)

    def test_should_have_the_correct_fields(self):
        with open('customers.xml', 'r') as file:
            data= file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        fields = [row.get('name') for row in soup.find_all('row')]
        correct_fields = ['email', 'first_name', 'id', 'city', 'last_name']
        fields.sort()
        correct_fields.sort()
        self.assertEqual(fields, correct_fields)
