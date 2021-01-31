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

from models.fixture import Fixture

# Declare a route for the list of fixtures and display them
@fixtures_blueprint.route("/fixtures")
def fixures():
    fixtures = fixture_repository.select_all()
    teams = team_repository.select_all()

    return render_template("fixtures/show.html", fixtures=fixtures, teams = teams)

# Declare a route for the list of fixtures and display them
@fixtures_blueprint.route("/fixtures/maintenance")
def fixure_maintenance():
    fixtures = fixture_repository.select_all()
    teams = team_repository.select_all()

    return render_template("fixtures/maintenance.html", fixtures=fixtures, teams = teams)

# Route for adding fixture to league
@fixtures_blueprint.route("/fixtures/new", methods=["GET"])
def new_fixture():
    return render_template("fixtures/new.html")

# CREATE
# POST '/fixtures'
@fixtures_blueprint.route("/fixtures", methods=['POST'])
def create_fixture():
    home_team_id = request.form['home_team_id']
    away_team_id = request.form['away_team_id']
    fixture_date = request.form['fixture_date']

    fixture_result = None
    league_id = 1

    fixture = Fixture(home_team_id, away_team_id, fixture_date, fixture_result, league_id)
    fixture_repository.save(fixture)
    return redirect('/fixtures')