# galaxy classifier 
from sklearn.cluster import KMeans

def assign_populations(gal, n_clusters=2):
    X = gal[["g_r", "r"]].values

    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    gal["pop"] = kmeans.fit_predict(X)

    return gal

