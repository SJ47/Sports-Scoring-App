from db.run_sql import run_sql
from models.league import League
from models.team import Team


# Get teams in the selected league
def select_all():
    teams = []

    sql = "SELECT * FROM teams"
    
    results = run_sql(sql)

    for row in results:
        team = Team(row['team_name'], row['league_id'], row['id'])
        teams.append(team)

    return teams
