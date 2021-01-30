# Import flask and render template
from flask import Flask, render_template

# import Blueprint class from flask
from flask import Blueprint

# Import repositories
# import repositories.league_repository as league_repository

# Create a new instance of Blueprint called "admin"
admin_blueprint = Blueprint("admin", __name__)

# Declare a route for the admin page
@admin_blueprint.route("/admin")
def admin():
    return render_template("admin/index.html")
