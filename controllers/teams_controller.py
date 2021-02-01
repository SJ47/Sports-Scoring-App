import pdb 
# Import flask and render template
from flask import Flask, render_template, request, redirect

# import Blueprint class from flask
from flask import Blueprint

# Create a new instance of Blueprint called "fixtures"
teams_blueprint = Blueprint("teams", __name__)

# Import repositories
import repositories.league_repository as league_repository
import repositories.team_repository as team_repository
from models.team import Team


# Declare a route for the teams page
@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html", all_teams = teams)

# Route for adding team to league
@teams_blueprint.route("/teams/new", methods=["GET"])
def new_team():
    return render_template("teams/new.html")

# CREATE
# POST '/teams'
@teams_blueprint.route("/teams", methods=['POST'])
def create_team():
    team_name = request.form['team_name']
    league_id = 1
    team = Team(team_name, league_id)
    team_repository.save(team)
    return redirect('/teams')

# DELETE
# DELETE '/teams/<id>'
@teams_blueprint.route("/teams/<id>/delete", methods=['POST'])
def delete_team(id):
    team_repository.delete(id)
    return redirect('/teams')

# EDIT
# GET 'teams/<id>/edit' 
@teams_blueprint.route("/teams/<id>/edit", methods=['GET'])
def edit_team(id):
    team = team_repository.select(id)
    return render_template('teams/edit.html', team=team)
    
# UPDATE
# PUT '/teams/<id>'
@teams_blueprint.route("/teams/<id>", methods=['POST'])
def update_team(id):
    team_name = request.form['team_name']
    league_id = 1
    team = Team(team_name, league_id, id)
    team_repository.update(team)
    return redirect('/teams')
