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
    return render_template("leagues/show.html", teams = teams, stats = stats, games_won = games_won)


