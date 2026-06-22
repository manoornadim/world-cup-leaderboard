import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FOOTBALL_DATA_API_KEY")

URL = "https://api.football-data.org/v4/competitions/WC/matches"


def load_results():

    headers = {
        "X-Auth-Token": API_KEY
    }

    response = requests.get(URL, headers=headers)

    if response.status_code != 200:
        raise Exception(
            f"Football API error: {response.status_code} - {response.text}"
        )

    data = response.json()

    matches = []

    for match in data["matches"]:

        # Ignore matches that haven't finished
        if match["status"] != "FINISHED":
            continue

        matches.append({
            "Date": match["utcDate"],
            "Group": match["group"],

            "Home Team": match["homeTeam"]["name"],
            "Home Score": match["score"]["fullTime"]["home"],

            "Away Score": match["score"]["fullTime"]["away"],
            "Away Team": match["awayTeam"]["name"]
        })

    return pd.DataFrame(matches)