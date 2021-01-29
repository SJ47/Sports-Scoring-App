import unittest
from models.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Jim", "MacHeader", 1, 10, 3, 1)
        
    def test_player_has_name(self):
        self.assertEqual("Jim MacHeader", self.player.first_name + " " + self.player.last_name)

    def test_player_has_team_id(self):
        self.assertEqual(1, self.player.team_id)

    def test_player_number_of_goals_scored(self):
        self.assertEqual(10, self.player.goals_scored)

    def test_player_number_of_yellow_cards(self):
        self.assertEqual(3, self.player.yellow_cards)

    def test_player_number_of_red_cards(self):
        self.assertEqual(1, self.player.red_cards)

