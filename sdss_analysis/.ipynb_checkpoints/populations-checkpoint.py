import numpy as np

def assign_populations(df, threshold=2.2):
    """
    Separate galaxies into red and blue populations using u-r color.
    """
    df = df.copy()
    df["population"] = np.where(df["u_r"] > threshold, "red", "blue")
    return df
