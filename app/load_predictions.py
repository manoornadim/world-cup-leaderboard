import os
import pandas as pd

PREDICTIONS_DIR = "data/predictions"

def load_all_predictions():
    """
    Loads all participant prediction Excel files.
    Returns:
        dict: {participant_name: DataFrame}
    """

    all_data = {}

    for file in os.listdir(PREDICTIONS_DIR):
        if file.endswith(".xlsx") or file.endswith(".xls"):

            participant_name = file.replace(".xlsx", "").replace(".xls", "")
            file_path = os.path.join(PREDICTIONS_DIR, file)

            df = pd.read_excel(file_path)

            # Standardise column names (strip spaces just in case)
            df.columns = [col.strip() for col in df.columns]

            # Keep only relevant columns
            df = df[[
                "Date",
                "Group",
                "Home Team",
                "Pred Home",
                "Pred Away",
                "Away Team"
            ]]

            all_data[participant_name] = df

    return all_data
