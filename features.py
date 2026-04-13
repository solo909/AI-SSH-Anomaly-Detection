import pandas as pd

def build_features(df):
    features = df.groupby("ip").agg(
        failed_attempts=("status", lambda x: (x == "failed").sum()),
        successful_attempts=("status", lambda x: (x == "success").sum()),
        total_attempts=("status", "count")
    ).reset_index()

    return features