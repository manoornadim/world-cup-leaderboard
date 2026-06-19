import pandas as pd

RESULTS_PATH = "data/results/results.xlsx"

def load_results():
    """
    Loads official match results.
    Expected columns:
        Date, Group, Home Team, Home Score, Away Score, Away Team
    """

    df = pd.read_excel(RESULTS_PATH)

    df.columns = [col.strip() for col in df.columns]

    required_cols = [
        "Date",
        "Group",
        "Home Team",
        "Home Score",
        "Away Score",
        "Away Team"
    ]

    df = df[required_cols]

    return df

