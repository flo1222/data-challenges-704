# pylint: disable-all
import unittest
from subqueries import display_best_buyers
import sqlite3

conn = sqlite3.connect('db/ecommerce.db')
db = conn.cursor()


class TestBestCustomers(unittest.TestCase):
    def test_length_results(self):
        results = display_best_buyers(db)
        self.assertEqual(len(results), 3)

    def test_results(self):
        results = display_best_buyers(db)
        expected = [(1031.24, 2), (2175.03, 4), (1096.3, 5)]
        self.assertEqual(results, expected)

    def test_type_results(self):
        results = display_best_buyers(db)
        self.assertIsInstance(results, list)
