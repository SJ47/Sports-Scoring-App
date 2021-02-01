from db.run_sql import run_sql
from models.league import League
from models.team import Team


# Select_all() teams
def select_all():
    teams = []

    sql = "SELECT * FROM teams"
    
    results = run_sql(sql)

    for row in results:
        team = Team(row['team_name'], row['league_id'], row['id'])
        teams.append(team)

    return teams

# Save team
def save(team):
    sql = "INSERT INTO teams(team_name, league_id) VALUES ( %s, %s ) RETURNING id"
    values = [team.team_name, team.league_id]
    results = run_sql( sql, values )
    team.id = results[0]['id']
    return team

# Delete one team by id
def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# Update team
def update(team):
    sql = "UPDATE teams SET (team_name, league_id) = (%s, %s) WHERE id = %s"
    values = [team.team_name, team.league_id, team.id]
    run_sql(sql, values)

def select(id):
    team = None
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        team = Team(result['team_name'], result['league_id'], result['id'] )
    return team