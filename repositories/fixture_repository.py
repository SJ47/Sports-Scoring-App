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

# Save fixture
def save(fixture):
    sql = "INSERT INTO fixtures(home_team_id, away_team_id, fixture_date, fixture_result, league_id) VALUES ( %s, %s, %s, %s, %s ) RETURNING id"
    values = [fixture.home_team_id, fixture.away_team_id, fixture.fixture_date, fixture.fixture_result, fixture.league_id]
    results = run_sql( sql, values )
    fixture.id = results[0]['id']
    return fixture

# Delete one fixture by id
def delete(id):
    sql = "DELETE FROM fixtures WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# Select a fixture
def select(id):
    fixture = None
    sql = "SELECT * FROM fixtures WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        fixture = Fixture(result['home_team_id'], result['away_team_id'], result['fixture_date'], result['fixture_result'], result['league_id'], result['id'] )
    return fixture

# Update fixture
def update(fixture):
    sql = "UPDATE fixtures SET (home_team_id, away_team_id, fixture_date, fixture_result, league_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [fixture.home_team_id, fixture.away_team_id, fixture.fixture_date, fixture.fixture_result, fixture.league_id, fixture.id]
    run_sql(sql, values)