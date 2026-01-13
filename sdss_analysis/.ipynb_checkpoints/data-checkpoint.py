import pandas as pd

def load_galaxies(path="data/sdss.csv"):
    """
    Load SDSS galaxy data and apply basic cleaning.
    """
    df = pd.read_csv(path)

    # Keep only galaxies
    df = df[df["class"] == "GALAXY"].copy()

    # Remove missing values
    df = df.dropna(subset=["u", "g", "r", "i", "z", "redshift"])

    return df
