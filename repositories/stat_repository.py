# Generate all stats from team each time show leagues is run

import pdb

# from db.run_sql import run_sql
from models.league import League
from models.team import Team
from models.fixture import Fixture
from models.stat import Stat

# from operator import itemgetter

def generate_stats(teams, fixtures):
    stats = []
    # games_won_list = []

    # Loop through every team
    for team in teams:
        
        #### Loop through every fixture and pick out that teams fixtures that have been played (eg. have a result !none)
        games_played = 0
        for fixture in fixtures:
            if fixture.fixture_result == None or fixture.fixture_result == "":
                pass
            else:
                # Check if the current team in the loop is involved in the fixture
                if team.id == fixture.home_team_id or team.id == fixture.away_team_id:
                    games_played += 1
                    # pdb.set_trace()
        
        # pdb.set_trace() 
        stats.append({team.id:games_played})
        
    return stats


def generate_games_won(teams, fixtures):
    games_won_list = []

    # Loop through every team
    for team in teams:

        #### work out games won
        games_won = 0
        for fixture in fixtures:

            # Pass if scores is none
            if fixture.fixture_result == None or fixture.fixture_result=="":
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
    # pdb.set_trace()   
    return games_won_list

## Calculate games drawn
def generate_games_drawn(teams, fixtures):
    games_drawn_list = []

    # Loop through every team
    for team in teams:

        #### work out games drawn
        games_drawn = 0
        for fixture in fixtures:

            # Pass if scores is none
            if fixture.fixture_result == None or fixture.fixture_result=="":
                pass
            else:
                # Check if the current team in the loop is involved in the fixture
                if team.id == fixture.home_team_id or team.id == fixture.away_team_id:
                    
                    # Convert scores from strings to integers for calculations
                    home_score = int(fixture.fixture_result[0:1])
                    away_score = int(fixture.fixture_result[2:3])
                    
                    # If team is home team and home score is drawn add to games_drawn
                    if team.id == fixture.home_team_id and home_score == away_score:
                        games_drawn += 1
                    
                    # If team is away team and away score is equal add to games_drawn
                    elif team.id == fixture.away_team_id and away_score == home_score:
                        games_drawn += 1
                    else:
                        pass          

        games_drawn_list.append({team.id:games_drawn})

    return games_drawn_list

## Calculate games lost
def generate_games_lost(teams, fixtures):
    games_lost_list = []

    # Loop through every team
    for team in teams:

        #### work out games lost
        games_lost = 0
        for fixture in fixtures:

            # Pass if scores is none
            if fixture.fixture_result == None or fixture.fixture_result=="":
                pass
            else:
                # Check if the current team in the loop is involved in the fixture
                if team.id == fixture.home_team_id or team.id == fixture.away_team_id:
                    
                    # Convert scores from strings to integers for calculations
                    home_score = int(fixture.fixture_result[0:1])
                    away_score = int(fixture.fixture_result[2:3])
                    
                    # If team is home team and home score is less than add to games_lost
                    if team.id == fixture.home_team_id and home_score < away_score:
                        games_lost += 1
                    
                    # If team is away team and away score is less than add to games_lost
                    elif team.id == fixture.away_team_id and away_score < home_score:
                        games_lost += 1
                    else:
                        pass          

        games_lost_list.append({team.id:games_lost})

    return games_lost_list


## Calculate goals for
def generate_goals_for(teams, fixtures):
    goals_for_list = []

    # Loop through every team
    for team in teams:

        #### work out games lost
        goals_for = 0
        for fixture in fixtures:

            # Pass if scores is none
            if fixture.fixture_result == None or fixture.fixture_result=="":
                pass
            else:
                # Check if the current team in the loop is involved in the fixture
                if team.id == fixture.home_team_id or team.id == fixture.away_team_id:
                    
                    # Convert scores from strings to integers for calculations
                    home_score = int(fixture.fixture_result[0:1])
                    away_score = int(fixture.fixture_result[2:3])
                    
                    # If team is home team add any goals scored to goals_for
                    if team.id == fixture.home_team_id:
                        goals_for += home_score
                    
                    # If team is away team add any goals scored to goals_for
                    elif team.id == fixture.away_team_id:
                        goals_for += away_score
                    else:
                        pass          

        goals_for_list.append({team.id:goals_for})

    return goals_for_list

## Calculate goals against
def generate_goals_against(teams, fixtures):
    goals_against_list = []

    # Loop through every team
    for team in teams:

        #### work out games lost
        goals_against = 0
        for fixture in fixtures:

            # Pass if scores is none
            if fixture.fixture_result == None or fixture.fixture_result=="":
                pass
            else:
                # Check if the current team in the loop is involved in the fixture
                if team.id == fixture.home_team_id or team.id == fixture.away_team_id:
                    
                    # Convert scores from strings to integers for calculations
                    home_score = int(fixture.fixture_result[0:1])
                    away_score = int(fixture.fixture_result[2:3])
                    
                    # If team is home team add any goals scored by away team to goals_against
                    if team.id == fixture.home_team_id:
                        goals_against += away_score
                    
                    # If team is away team add any goals scored by home team to goals_against
                    elif team.id == fixture.away_team_id:
                        goals_against += home_score
                    else:
                        pass          

        goals_against_list.append({team.id:goals_against})

    return goals_against_list

### Calculate form of last 5 games
def generate_games_form(teams, fixtures):
    games_form_list = []

    # Loop through every team
    for team in teams:

        #### work out form
        games_form = "-----"
        for fixture in fixtures:

            # Pass if scores is none
            if fixture.fixture_result == None or fixture.fixture_result=="":
                pass
            else:
                # Check if the current team in the loop is involved in the fixture
                if team.id == fixture.home_team_id or team.id == fixture.away_team_id:
                    
                    # Convert scores from strings to integers for calculations
                    home_score = int(fixture.fixture_result[0:1])
                    away_score = int(fixture.fixture_result[2:3])
                    
                    # If team is home team and home score is greater add form-W
                    if team.id == fixture.home_team_id and home_score > away_score:
                        games_form+=("W")
                    
                    # If team is away team and away score is greater add to form-W
                    elif team.id == fixture.away_team_id and away_score > home_score:
                        games_form+=("W")

                    # If team is home team and home score is lose add to form-L
                    elif team.id == fixture.home_team_id and home_score < away_score:
                        games_form+=("L")
                    
                    # If team is away team and away score is lose add to form-L
                    elif team.id == fixture.away_team_id and away_score < home_score:
                        games_form+=("L")

                    # If team is away team and score is a draw add to form-D
                    elif team.id == fixture.home_team_id and away_score == home_score:
                        games_form += ("D")
                        
                    # If team is away team and score is a draw add to form-D
                    elif team.id == fixture.away_team_id and away_score == home_score:
                        games_form+=("D")
                    else:
                        pass          
                
        games_form_list.append({team.id:games_form})
                
        # pdb.set_trace() 
    # pdb.set_trace()   
    return games_form_list


## Calculate league points
def generate_league_points(teams, fixtures):
    league_points_list = []

    # Loop through every team
    for team in teams:

        #### work out points
        league_points = 0
        for fixture in fixtures:

            # Pass if scores is none
            if fixture.fixture_result == None or fixture.fixture_result=="":
                pass
            else:
                # Check if the current team in the loop is involved in the fixture
                if team.id == fixture.home_team_id or team.id == fixture.away_team_id:
                    
                    # Convert scores from strings to integers for calculations
                    home_score = int(fixture.fixture_result[0:1])
                    away_score = int(fixture.fixture_result[2:3])
                    
                    # If team is home team and home score is greater then add 3 points
                    if team.id == fixture.home_team_id and home_score > away_score:
                        league_points += 3
                    
                    # If team is away team and away score is greater then add 3 points
                    elif team.id == fixture.away_team_id and away_score > home_score:
                        league_points += 3

                    # If team is home team and home score a draw then add 1 point
                    elif team.id == fixture.home_team_id and home_score == away_score:
                        league_points += 1
                    
                    # If team is away team and away score a draw then add 1 point
                    elif team.id == fixture.away_team_id and away_score == home_score:
                        league_points += 1

                    else:
                        pass          

        league_points_list.append({team.id: league_points})

        # league_points_list = sorted(league_points_list, key=lambda k: k[team.id])
        # res = {val[0]: val[1] for val in sorted(test_dict.items(), key=lambda x: (-x[1], x[0]))}
        
    # res = {val[0] : val[1] for val in sorted(league_points_list, key = lambda x: (-x[1], x[0]))}


    # league_points_list=[{1: 8}, {3: 4}, {6: 3}, {7: 3}, {10: 3}, {2: 2}, {4: 1}, {11: 1}, {12: 1}, {5: 0}, {8: 0}, {9: 0}]
    # pdb.set_trace()
    return league_points_list
