from sklearn.ensemble import IsolationForest
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

def run_isolation_forest(features_df):

    df = features_df.copy() # copy data so original is unchanged