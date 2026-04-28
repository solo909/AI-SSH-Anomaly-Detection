from sklearn.ensemble import IsolationForest
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

FEATURE_COLS = ["failed_attempts", "unique_users", "duration_seconds", "attempt_rate"]

def run_isolation_forest(features_df, contamination=0.05):
    df = features_df.copy()

    X = df[FEATURE_COLS].fillna(0)
    X_scaled = StandardScaler().fit_transform(X)

    model = IsolationForest(contamination=contamination, random_state=42)
    df["if_anomaly"] = model.fit_predict(X_scaled)           # -1 = anomaly, 1 = normal
    df["if_flag"] = (df["if_anomaly"] == -1).astype(int)

    return df

def run_dbscan(features_df, eps=1.5, min_samples=2):
    df = features_df.copy()

    X = df[FEATURE_COLS].fillna(0)
    X_scaled = StandardScaler().fit_transform(X)

    model = DBSCAN(eps=eps, min_samples=min_samples)
    df["dbscan_cluster"] = model.fit_predict(X_scaled)       # -1 = outlier
    df["dbscan_flag"] = (df["dbscan_cluster"] == -1).astype(int)

    return df
