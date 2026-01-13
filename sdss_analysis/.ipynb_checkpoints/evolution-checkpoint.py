import pandas as pd
import numpy as np

def add_redshift_bins(df):
    """
    Bin galaxies in redshift.
    """
    df = df.copy()
    bins = [0, 0.05, 0.1, 0.2, 0.4, 1.0]
    df["z_bin"] = pd.cut(df["redshift"], bins=bins)
    return df

def color_statistics(df):
    """
    Compute mean u-r color and uncertainties in each redshift bin.
    """
    stats = df.groupby("z_bin")["u_r"].agg(["mean", "std", "count"])
    stats["stderr"] = stats["std"] / np.sqrt(stats["count"])
    return stats
