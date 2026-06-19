# loads official match results from the results.xlsx file

# import necessary libraries
import pandas as pd

# define the path to the results Excel file
RESULTS_PATH = "data/results/results.xlsx"

# define a function to load the official match results
def load_results():
    """
    Loads official match results.
    Expected columns:
        Date, Group, Home Team, Home Score, Away Score, Away Team
    """

    # read the Excel file into a DataFrame (a table-like structure)
    df = pd.read_excel(RESULTS_PATH)

    # remove any whitespace from column names
    df.columns = [col.strip() for col in df.columns]

    # select only the relevant columns
    required_cols = [
        "Date",
        "Group",
        "Home Team",
        "Home Score",
        "Away Score",
        "Away Team"
    ]

    # filter the DataFrame to include only the required columns
    df = df[required_cols]

    # return the DataFrame containing the official match results
    return df

