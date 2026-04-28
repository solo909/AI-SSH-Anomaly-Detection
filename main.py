from parser import parse_log
from features import build_features
from baseline import rule_based_detection
from models import run_isolation_forest, run_dbscan

file_path = "data/auth2.log"

df = parse_log(file_path)
print("RAW LOG DATA")
print(df)
print()

features_df = build_features(df)
print("FEATURE DATA")
print(features_df)
print()

result_df = rule_based_detection(features_df)
flagged = result_df[result_df["rule_flag"] == 1]
print("BASELINE RESULT")
print(f"{len(flagged)} IPs flagged out of {len(result_df)}")
print(flagged[["ip", "failed_attempts", "unique_users", "attempt_rate"]])
print()

if_df = run_isolation_forest(features_df)
flagged_if = if_df[if_df["if_flag"] == 1]
print("ISOLATION FOREST ANOMALIES")
print(f"{len(flagged_if)} IPs flagged out of {len(if_df)}")
print(flagged_if[["ip", "failed_attempts", "unique_users", "duration_seconds"]])
print()

dbscan_df = run_dbscan(features_df)
flagged_dbscan = dbscan_df[dbscan_df["dbscan_flag"] == 1]
print("DBSCAN OUTLIERS")
print(f"{len(flagged_dbscan)} IPs flagged out of {len(dbscan_df)}")
print(flagged_dbscan[["ip", "failed_attempts", "unique_users", "duration_seconds"]])