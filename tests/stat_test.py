import unittest
from models.stat import Stat

class TestStat(unittest.TestCase):
    def setUp(self):
        self.stat = Stat(15, 10, 4, 1, 28, 8, 20, 34)

    def test_stat_has_games_played(self):
        self.assertEqual(15, self.stat.played)

    def test_stat_has_games_won(self):
        self.assertEqual(10, self.stat.won)

    def test_stat_has_games_drawn(self):
        self.assertEqual(4, self.stat.drawn)

    def test_stat_has_games_lost(self):
        self.assertEqual(1, self.stat.lost)

    def test_stat_has_goals_for(self):
        self.assertEqual(28, self.stat.goals_for)

    def test_stat_has_goals_against(self):
        self.assertEqual(8, self.stat.goals_against)

    def test_stat_has_goals_difference(self):
        self.assertEqual(20, self.stat.goals_difference)

    def test_stat_has_points(self):
        self.assertEqual(34, self.stat.points)