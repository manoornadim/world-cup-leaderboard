# This is the main entry point for the Flask application.
# It sets up the routes and serves the static files for the web interface.

# import necessary libraries
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from app.scoring import calculate_leaderboard
import os
from app.load_predictions import load_todays_predictions

# create the Flask app and enable CORS, pointing to the static folder for the web interface
app = Flask(__name__, static_folder="../web")
CORS(app)

# define the route for the home page, serving the index.html file
# essentially, this is the main entry point for the web interface
@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")

# define a route to serve static files (like CSS, JS, images) from the static folder
@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(app.static_folder, path)

# define a route to get the leaderboard data in JSON format
@app.route("/api/leaderboard")
def leaderboard():
    return jsonify(calculate_leaderboard())

# define a route to get today's predictions in JSON format
@app.route("/api/todays-predictions")
def todays_predictions():
    return jsonify(load_todays_predictions())

# define a route to get the leaderboard data in JSON format
# starts website locally on port 5000 with debug mode enabled
if __name__ == "__main__":
    app.run(debug=True)