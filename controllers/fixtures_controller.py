# Import flask and render template
from flask import Flask, render_template, request, redirect

# import Blueprint class from flask
from flask import Blueprint

# Create a new instance of Blueprint called "fixtures"
fixtures_blueprint = Blueprint("fixtures", __name__)

# Import repositories
import repositories.league_repository as league_repository
import repositories.fixture_repository as fixture_repository
import repositories.team_repository as team_repository


# Declare a route for the list of fixtures and display them
@fixtures_blueprint.route("/fixtures")
def fixures():
    fixtures = fixture_repository.select_all()
    teams = team_repository.select_all()

    return render_template("fixtures/show.html", fixtures=fixtures, teams = teams)
