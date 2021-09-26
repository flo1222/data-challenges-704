# pylint: disable-all
import unittest
from query import movie_duration_buckets, longest_movies_by_director,\
    top_3_longest
import sqlite3

conn = sqlite3.connect('db/movies.sqlite')
db = conn.cursor()


class TestQuery(unittest.TestCase):
    def test_movie_duration_buckets(self):
        res = movie_duration_buckets(db)
        solution = [
            (30, 292),
            (60, 764),
            (90, 1362),
            (120, 5302),
            (150, 1617),
            (180, 331),
            (210, 88),
            (240, 19),
            (270, 7),
            (300, 11),
            (330, 4),
            (360, 7),
            (390, 7),
            (420, 4),
            (450, 4),
            (480, 2),
            (540, 4),
            (570, 3),
            (600, 4),
            (630, 2),
            (690, 2),
            (900, 1),
            (1020, 1)
        ]
        self.assertIs(type(solution), list)
        self.assertIs(type(solution[0]), tuple)
        self.assertEqual(res, solution)

    def test_longest_movies_by_director(self):
        res = longest_movies_by_director(db, "X")
        solution = [
            ('Of Gods and Men', 'Xavier Beauvois', 122, 1),
            ('Laurence Anyways', 'Xavier Dolan', 168, 1),
            ('Mommy', 'Xavier Dolan', 139, 2),
            ('Tom at the Farm', 'Xavier Dolan', 102, 3),
            ('Heartbeats', 'Xavier Dolan', 101, 4),
            ("It's Only the End of the World", 'Xavier Dolan', 97, 5),
            ('I Killed My Mother', 'Xavier Dolan', 96, 6),
            ('The Divide', 'Xavier Gens', 112, 1),
            ('Frontier(s)', 'Xavier Gens', 108, 2),
            ('Hitman', 'Xavier Gens', 100, 3)
        ]
        self.assertIs(type(solution), list)
        self.assertIs(type(solution[0]), tuple)
        self.assertEqual(res, solution)

    def test_top_3_longest(self):
        res = top_3_longest(db, "X")
        solution = [
            ('Of Gods and Men', 'Xavier Beauvois', 122, 1),
            ('Laurence Anyways', 'Xavier Dolan', 168, 1),
            ('Mommy', 'Xavier Dolan', 139, 2),
            ('Tom at the Farm', 'Xavier Dolan', 102, 3),
            ('The Divide', 'Xavier Gens', 112, 1),
            ('Frontier(s)', 'Xavier Gens', 108, 2),
            ('Hitman', 'Xavier Gens', 100, 3)
        ]
        self.assertIs(type(solution), list)
        self.assertIs(type(solution[0]), tuple)
        self.assertEqual(res, solution)
