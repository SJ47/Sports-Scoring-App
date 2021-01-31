# Generate all stats from team each time show leagues is run

import pdb

# from db.run_sql import run_sql
from models.league import League
from models.team import Team
from models.fixture import Fixture
from models.stat import Stat


def generate_stats(teams, fixtures):
    stats = []
    games_won_list = []

    # Loop through every team
    for team in teams:
       
        
        #### Loop through every fixture and pick out that teams fixtures that have been played (eg. have a result !none)
        games_played = 0
        for fixture in fixtures:
            if fixture.fixture_date == None:
                pass
            else:
                # Check if the current team in the loop is involved in the fixture
                if team.id == fixture.home_team_id or team.id == fixture.away_team_id:
                    games_played += 1
                    # pdb.set_trace()
        
        # pdb.set_trace() 
        stats.append({team.id:games_played})
        

        #### work out games won
        games_won = 0
        for fixture in fixtures:

            # Pass if scores is none
            if fixture.fixture_result == None:
                pass
            else:
                # Check if the current team in the loop is involved in the fixture
                if team.id == fixture.home_team_id or team.id == fixture.away_team_id:
                    
                    # Convert scores from strings to integers for calculations
                    home_score = int(fixture.fixture_result[0:1])
                    away_score = int(fixture.fixture_result[2:3])
                    
                    # If team is home team and home score is greater add to games_won
                    if team.id == fixture.home_team_id and home_score > away_score:
                        games_won += 1
                    
                    # If team is away team and away score is greater add to games_won
                    elif team.id == fixture.away_team_id and away_score > home_score:
                        games_won += 1
                    else:
                        pass          

        games_won_list.append({team.id:games_won})
                
        # pdb.set_trace() 
    # stats.append(games_won_list)
    # pdb.set_trace()   
    return stats