import pandas as pd
from app.load_predictions import load_all_predictions
from app.load_results import load_results


def get_result(home, away):

    if home > away:
        return "H"
    elif away > home:
        return "A"
    return "D"


def score_match(pred_home, pred_away, actual_home, actual_away):

    if pred_home == actual_home and pred_away == actual_away:
        return 3

    if get_result(pred_home, pred_away) == get_result(actual_home, actual_away):
        return 1

    return 0


def calculate_leaderboard():

    predictions = load_all_predictions()
    results = load_results()

    results_dict = {}

    for _, row in results.iterrows():

        # skip unplayed matches
        if pd.isna(row["Home Score"]) or pd.isna(row["Away Score"]):
            continue

        key = (
            str(row["Date"]),
            row["Home Team"],
            row["Away Team"]
        )

        results_dict[key] = {
            "home_score": row["Home Score"],
            "away_score": row["Away Score"]
        }

    leaderboard = []

    for player, df in predictions.items():

        total_points = 0

        for _, row in df.iterrows():

            key = (
                str(row["Date"]),
                row["Home Team"],
                row["Away Team"]
            )

            if key not in results_dict:
                continue

            actual = results_dict[key]

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

    return sorted(leaderboard, key=lambda x: x["points"], reverse=True)