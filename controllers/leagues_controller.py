# Import flask and render template
from flask import Flask, render_template

# import Blueprint class from flask
from flask import Blueprint

# Import repositories
import repositories.league_repository as league_repository
import repositories.team_repository as team_repository

# Create a new instance of Blueprint called "leagues"
leagues_blueprint = Blueprint("leagues", __name__)

# Declare a route for the list of leagues and display them
@leagues_blueprint.route("/leagues")
def leagues():
    teams = team_repository.select_all()

    return render_template("leagues/show.html", teams = teams)


