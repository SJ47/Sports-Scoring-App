import unittest
from models.fixture import Fixture

class TestFixture(unittest.TestCase):
    def setUp(self):
        self.fixture = Fixture(1, 2, "20-01-2021", None, 1)
        self.fixture_with_result = Fixture(1, 2, "20-01-2021", "2-0", 1)
    
    def test_fixture_has_home_team_id(self):
        self.assertEqual(1, self.fixture.home_team_id)
    
    def test_fixture_has_away_team_id(self):
        self.assertEqual(2, self.fixture.away_team_id)

    def test_fixture_has_fixture_date(self):
        self.assertEqual("20-01-2021", self.fixture.fixture_date)

    def test_fixture_has_fixture_result(self):
        self.assertEqual("2-0", self.fixture_with_result.fixture_result)

    def test_fixture_has_no_fixture_result(self):
        self.assertEqual(None, self.fixture.fixture_result)

    def test_fixture_has_league_id(self):
        self.assertEqual(1, self.fixture.league_id)
