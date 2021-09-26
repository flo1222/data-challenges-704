# pylint: disable-all
import unittest
from subqueries import get_average_purchase
import sqlite3

conn = sqlite3.connect('db/ecommerce.db')
db = conn.cursor()


class TestAveragePerCustomer(unittest.TestCase):
    def test_length_results(self):
        results = get_average_purchase(db)
        self.assertEqual(len(results), 5)

    def test_results(self):
        results = get_average_purchase(db)
        expected = [(673.9, 1), (1031.24, 2), (266.32, 3), (2175.03, 4), (1096.3, 5)]
        self.assertEqual(results, expected)

    def test_type_results(self):
        results = get_average_purchase(db)
        self.assertIsInstance(results, list)
