import pdb, operator
from operator import itemgetter
from datetime import datetime

# Import flask and render template
from flask import Flask, render_template

# import Blueprint class from flask
from flask import Blueprint

# Import repositories
import repositories.league_repository as league_repository
import repositories.team_repository as team_repository
import repositories.stat_repository as stat_repository
import repositories.fixture_repository as fixture_repository

# Create a new instance of Blueprint called "leagues"
leagues_blueprint = Blueprint("leagues", __name__)

# Declare a route for the list of leagues and display them
@leagues_blueprint.route("/leagues")
def leagues():
    teams = team_repository.select_all()
    fixtures = fixture_repository.select_all()
    stats = stat_repository.generate_stats(teams, fixtures)
    games_won = stat_repository.generate_games_won(teams, fixtures)
    games_drawn = stat_repository.generate_games_drawn(teams, fixtures)
    games_lost = stat_repository.generate_games_lost(teams, fixtures)
    goals_for = stat_repository.generate_goals_for(teams, fixtures)
    goals_against = stat_repository.generate_goals_against(teams, fixtures)
    games_form = stat_repository.generate_games_form(teams, fixtures)

    league_points = stat_repository.generate_league_points(teams, fixtures)
    today = datetime.now()
    today = today.strftime("%d/%m/%Y %H:%M:%S")

    # sorted_d = sorted(d.items(), key=operator.itemgetter(1))
    # sorted_d = sorted(league_points, key=itemgetter(key))

    # pdb.set_trace()
    return render_template("leagues/show.html", teams = teams, stats = stats, games_won = games_won, games_drawn = games_drawn, games_lost = games_lost, league_points = league_points, goals_for = goals_for, goals_against = goals_against, games_form = games_form, today = today)

    # <!-- Points from games won and games drawn  -->
    # {{games_won[team.id-1][team.id]*3 + games_drawn[team.id-1][team.id]*1}}
