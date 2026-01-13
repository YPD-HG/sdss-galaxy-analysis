def add_colors(df):
    """
    Compute SDSS color indices.
    """
    df = df.copy()
    df["u_g"] = df["u"] - df["g"]
    df["g_r"] = df["g"] - df["r"]
    df["u_r"] = df["u"] - df["r"]
    return df
