# compare predictions to results and calculate leaderboard

# import necessary libraries
import pandas as pd
from app.load_predictions import load_all_predictions
from app.load_results_api import load_results

# helper functions

# clean team names and dates for consistent matching
def clean_team(name):
    return str(name).strip().lower().replace(" ", "")

# force date to a consistent format for matching
def clean_date(date):
    return pd.to_datetime(date).strftime("%Y-%m-%d")

# build a unique key for each match based on date and teams
def build_match_key(date, home, away):
    return f"{clean_date(date)}|{clean_team(home)}|{clean_team(away)}"

# determine the result of a match based on home and away scores
def get_result(home, away):
    if home > away:
        return "H"
    elif away > home:
        return "A"
    return "D"

# score a single match prediction against the actual result
def score_match(pred_home, pred_away, actual_home, actual_away):

    if pred_home == actual_home and pred_away == actual_away:
        return 3

    if get_result(pred_home, pred_away) == get_result(actual_home, actual_away):
        return 1

    return 0

# main function to calculate the leaderboard based on predictions and actual results
def calculate_leaderboard():

    # load all data
    predictions = load_all_predictions()
    results = load_results()

    # build a dictionary of actual match results for quick lookup
    results_dict = {}

    # build lookup of actual results
    for _, row in results.iterrows():

        # skip unplayed matches (where scores are NaN)
        if pd.isna(row["Home Score"]) or pd.isna(row["Away Score"]):
            continue

        # create a unique key for the match based on date and teams
        key = build_match_key(
            row["Date"],
            row["Home Team"],
            row["Away Team"]
        )

        # store the actual scores in the results dictionary
        results_dict[key] = {
            "home_score": row["Home Score"],
            "away_score": row["Away Score"]
        }

    # create empty leaderboard to store player scores
    leaderboard = []

    # iterate through each player's predictions and calculate their total points
    for player, df in predictions.items():

        # initialise total points for the player
        total_points = 0

        # loop through each match
        for _, row in df.iterrows():

            key = build_match_key(
                row["Date"],
                row["Home Team"],
                row["Away Team"]
            )

            # skip unplayed matches
            if key not in results_dict:
                continue

            actual = results_dict[key]

            # score the match and add to total points
            total_points += score_match(
                row["Pred Home"],
                row["Pred Away"],
                actual["home_score"],
                actual["away_score"]
            )


        leaderboard.append({
            "name": player,
            "points": int(total_points)
        })

    # sort the leaderboard by points in descending order
    return sorted(leaderboard, key=lambda x: x["points"], reverse=True)