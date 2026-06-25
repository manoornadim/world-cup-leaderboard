# collects all participant predictions from the data/predictions folder and returns a dictionary of DataFrames keyed by participant name

# import necessary libraries
import os
import pandas as pd

# define the path to the prediction files
PREDICTIONS_DIR = "data/predictions"

# define a function to load all predictions
def load_all_predictions():
    """
    Loads all participant prediction Excel files.
    Returns:
        dict: {participant_name: DataFrame}
    """
    # create an empty dictionary to hold all data
    all_data = {}

    # iterate through all files in the predictions directory
    for file in os.listdir(PREDICTIONS_DIR):
        # check if the file is an Excel file, otherwise ignore it
        if file.endswith(".xlsx") or file.endswith(".xls"):

            # extract participant name from the file name
            participant_name = file.replace(".xlsx", "").replace(".xls", "")
            # construct the full file path safely
            file_path = os.path.join(PREDICTIONS_DIR, file)

            # read the Excel file into a DataFrame (a table-like structure)
            df = pd.read_excel(file_path)

            # remove any whitespace from column names
            df.columns = [col.strip() for col in df.columns]

            # select only the relevant columns
            df = df[[
                "Date",
                "Group",
                "Home Team",
                "Pred Home",
                "Pred Away",
                "Away Team"
            ]]

            # store the DataFrame in the dictionary with participant name as the key
            all_data[participant_name] = df

    # return the dictionary containing all participant predictions
    return all_data

from datetime import datetime


def load_todays_predictions():

    all_predictions = load_all_predictions()

    today = datetime.today().strftime("%Y-%m-%d")

    todays_predictions = {}

    for player, df in all_predictions.items():

        # convert dates to consistent format
        df["Date"] = df["Date"].apply(
            lambda x: pd.to_datetime(x).strftime("%Y-%m-%d")
        )

        # keep only today's matches
        todays_df = df[df["Date"] == today]

        # convert to list of dictionaries for JSON
        todays_predictions[player] = todays_df.to_dict(
            orient="records"
        )

    return todays_predictions