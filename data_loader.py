import pandas as pd

def load_data(file_path):
    """Loads CSV data and preprocesses it."""
    df = pd.read_csv(file_path)
    df["Date"] = pd.to_datetime(df["Date"])  # Convert Date column to datetime
    return df
