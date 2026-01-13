# cosmic history engine

import pandas as pd

def add_redshift_bins(gal):
    bins = [0, 0.05, 0.1, 0.2, 0.4, 1.0]
    gal["z_bin"] = pd.cut(gal["redshift"], bins)
    return gal

def color_statistics(gal):
    stats = gal.groupby("z_bin")["u_r"].agg(["mean", "std", "count"])
    stats["stderr"] = stats["std"] / (stats["count"] ** 0.5)
    return stats
