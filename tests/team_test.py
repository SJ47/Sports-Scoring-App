import unittest
from models.team import Team

class TestTeam(unittest.TestCase):
    def setUp(self):
        self.team = Team("McVities United", 1)

    def test_team_has_team_name(self):
        self.assertEqual("McVities United", self.team.team_name)

    def test_team_has_league_id(self):
        self.assertEqual(1, self.team.league_id)
