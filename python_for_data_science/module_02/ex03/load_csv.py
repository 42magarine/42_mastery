import pandas as pd     # https://pandas.pydata.org/
from typing import Optional


def load(path: str) -> Optional[pd.DataFrame]:
    """
    Load a CSV file and return the dataset with dimension information.

    Args:
        path (str): Path to the CSV file.

    Returns:
        pd.DataFrame or None: Dataset if successful, None if there's an error.
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as error:
        print(f"Error: {error}")
        return None
