# pylint: disable-all
import unittest
from join_queries import best_employee
import sqlite3

conn = sqlite3.connect('db/ecommerce.sqlite')
db = conn.cursor()


class TestBestEmployee(unittest.TestCase):
    def test_length_results(self):
        results = best_employee(db)
        self.assertEqual(len(results), 1)

    def test_good_result(self):
        results = best_employee(db)
        expected = [('Patty', 'Lee', 7945.6)]
        self.assertEqual(results, expected)

    def test_type_result(self):
        results = best_employee(db)
        self.assertIsInstance(results, list)
