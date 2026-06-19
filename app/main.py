from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from scoring import calculate_leaderboard
import os

app = Flask(__name__, static_folder="../web")
CORS(app)


@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(app.static_folder, path)


@app.route("/api/leaderboard")
def leaderboard():
    return jsonify(calculate_leaderboard())


if __name__ == "__main__":
    app.run(debug=True)