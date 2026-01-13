# photometry module
def add_colors(gal):
    gal = gal.copy()

    gal["u_g"] = gal["u"] - gal["g"]
    gal["g_r"] = gal["g"] - gal["r"]
    gal["u_r"] = gal["u"] - gal["r"]

    return gal
