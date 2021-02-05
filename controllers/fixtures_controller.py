import pdb
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

    return render_template("fixtures/index.html", fixtures=fixtures, teams = teams)

# Route for showing fixtures
@fixtures_blueprint.route("/fixtures/show", methods=["GET"])
def show_fixtures():
    fixtures = fixture_repository.select_all()
    teams = team_repository.select_all()

    # pdb.set_trace()
    return render_template("fixtures/show.html", fixtures=fixtures, teams = teams)

# Route for adding fixture to league
@fixtures_blueprint.route("/fixtures/new", methods=["GET"])
def new_fixture():
    teams = team_repository.select_all()
    return render_template("fixtures/new.html", teams = teams)

# CREATE
# POST '/fixtures'
@fixtures_blueprint.route("/fixtures", methods=['POST'])
def create_fixture():
    home_team_id = request.form['home_team_id']
    away_team_id = request.form['away_team_id']
    fixture_date = request.form['fixture_date']
    fixture_result = request.form['fixture_result']

    # fixture_result = None
    league_id = 1

    fixture = Fixture(home_team_id, away_team_id, fixture_date, fixture_result, league_id)
    fixture_repository.save(fixture)
    return redirect('/fixtures')

# DELETE
# DELETE '/fixtures/<id>'
@fixtures_blueprint.route("/fixtures/<id>/delete", methods=['POST'])
def delete_fixture(id):
    fixture_repository.delete(id)
    return redirect('/fixtures')

# Route for showing a teams fixtures
@fixtures_blueprint.route("/fixtures/<id>/team_fixtures", methods=["GET"])
def show_team_fixtures(id):
    fixtures = fixture_repository.select_all()
    teams = team_repository.select_all()

    # pdb.set_trace()
    return render_template("fixtures/team_fixtures.html", fixtures=fixtures, teams=teams, team_name = id)
    

# # EDIT
# # GET 'fixtures/<id>/edit' 
@fixtures_blueprint.route("/fixtures/<id>/edit", methods=['GET'])
def edit_fixture(id):
    fixture = fixture_repository.select(id)

# changes to help add team names in edit fields instead of team IDs
    home_team = team_repository.select(fixture.home_team_id)
    away_team = team_repository.select(fixture.away_team_id)
# end changes
#   
    teams = team_repository.select_all()
    return render_template('fixtures/edit.html', fixture = fixture, home_team = home_team, away_team = away_team, teams = teams)
    
# # UPDATE
# # PUT '/fixtures/<id>'
@fixtures_blueprint.route("/fixtures/<id>", methods=['POST'])
def update_fixture(id):
    home_team_id = request.form['home_team_id']
    away_team_id = request.form['away_team_id']
    fixture_date = request.form['fixture_date']
    fixture_result = request.form['fixture_result']

    league_id = 1
    fixture = Fixture(home_team_id, away_team_id, fixture_date, fixture_result, league_id, id)
    fixture_repository.update(fixture)
    return redirect('/fixtures')
