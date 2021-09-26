# pylint: disable-all

import unittest
import sqlite3
from yaml import load, FullLoader
from os import path
from queries import directors_count, sorted_directors, love_movies,\
    directors_with_name, long_movies

conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()
with open(path.join(path.dirname(__file__), 'results.yml'), encoding='utf-8') as f:
    results = load(f, Loader=FullLoader)


class QueriesMethods(unittest.TestCase):
    def test_directors_count(self):
        count = directors_count(db)
        self.assertIs(type(count), int)
        self.assertEqual(count, 4092)

    def test_sorted_directors(self):
        directors_list = results['directors']
        response = sorted_directors(db)
        self.assertIs(type(response), list)
        self.assertEqual(response, directors_list)

    def test_love_movies(self):
        love_movies_list = results['love_movies']
        response = love_movies(db)
        self.assertIs(type(response), list)
        self.assertEqual(response, love_movies_list)

    def test_directors_with_name(self):
        directors_count = directors_with_name(db, "kubric")
        self.assertIs(type(directors_count), int)
        self.assertEqual(directors_count, 1)
        directors_count = directors_with_name(db, "john")
        self.assertEqual(directors_count, 131)

    def test_input_escaping(self):
        malicious_name = "/*malicious code*/you_should_prevent_sql_injection"
        directors_count = directors_with_name(db, malicious_name)
        self.assertEqual(directors_count, 0)

    def test_long_movies(self):
        long_movies_list = results['long_movies']
        response = long_movies(db, 300)
        self.assertIs(type(response), list)
        self.assertEqual(response, long_movies_list)
