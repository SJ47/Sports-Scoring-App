from db.run_sql import run_sql
from models.league import League
from models.team import Team
from models.fixture import Fixture


# Select all fixtures
def select_all():
    fixtures = []

    sql = "SELECT * FROM fixtures"
    
    results = run_sql(sql)

    for row in results:
        fixture = Fixture(row['home_team_id'], row['away_team_id'], row['fixture_date'], row['fixture_result'], row['league_id'], row['id'])
        fixtures.append(fixture)

    return fixtures