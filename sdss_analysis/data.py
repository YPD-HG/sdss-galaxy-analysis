import pandas as pd

def load_galaxies(path="data/Skyserver_SQL2_27_2018 6_51_39 PM.csv"):
    df = pd.read_csv(path)

    # Keep only galaxies
    gal = df[df["class"] == "GALAXY"].copy()

    # Convert columns to numeric
    cols = ["u", "g", "r", "i", "z", "redshift"]
    for c in cols:
        gal[c] = pd.to_numeric(gal[c], errors="coerce")

    # Drop bad rows
    gal = gal.dropna(subset=cols)

    return gal
