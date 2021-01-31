# Generate all stats from team each time show leagues is run

# from db.run_sql import run_sql
from models.league import League
from models.team import Team
from models.fixture import Fixture
from models.stat import Stat

def generate_stats(teams, fixtures):
    stats = []

    for team in teams:
        stats.append(10)

    
    
    return stats