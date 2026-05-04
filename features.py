import pandas as pd


def build_features(df):
    features = df.groupby("ip").agg(
        failed_attempts=("status", lambda x: (x == "failed").sum()),
        unique_users=("user", "nunique"),
        first_seen=("timestamp", "min"),
        last_seen=("timestamp", "max"),
    ).reset_index()

    features["duration_seconds"] = (
        features["last_seen"] - features["first_seen"]
    ).dt.total_seconds()

    features["attempt_rate"] = features.apply(
        lambda r: r["failed_attempts"] / max(r["duration_seconds"], 60),
        axis=1
    )

    features = features.drop(columns=["first_seen", "last_seen"])

    return features