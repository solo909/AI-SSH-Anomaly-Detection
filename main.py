from parser import parse_log
from features import build_features
from baseline import rule_based_detection
from models import run_isolation_forest, run_dbscan
import matplotlib.pyplot as plt

file_path = "data/auth2.log"

with open(file_path) as f:
   df = parse_log(f)
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


y_configs = [
   ("unique_users",     "Unique Users"),
   ("duration_seconds", "Duration (s)"),
   ("attempt_rate",     "Attempt Rate"),
]


tab10_red = plt.cm.tab10.colors[3]  
cluster_colors = [c for c in plt.cm.tab10.colors if c != tab10_red]


fig, axes = plt.subplots(len(y_configs), 3, figsize=(18, 5 * len(y_configs)))


for row_i, (y_col, y_label) in enumerate(y_configs):
   ax0, ax1, ax2 = axes[row_i]


   # Baseline
   ax0.scatter(result_df["failed_attempts"], result_df[y_col], c=["red" if f else "steelblue" for f in result_df["rule_flag"]], edgecolors="black", linewidths=0.5)
   for _, r in result_df.iterrows():
       ax0.annotate(r["ip"], (r["failed_attempts"], r[y_col]), fontsize=6, textcoords="offset points", xytext=(4, 4))
   ax0.scatter([], [], c="red", label="Flagged")
   ax0.scatter([], [], c="steelblue", label="Normal")
   ax0.set_xlabel("Failed Attempts")
   ax0.set_ylabel(y_label)
   ax0.set_title(f"Baseline — Failed Attempts vs {y_label}")
   ax0.legend()


   # Isolation Forest
   ax1.scatter(if_df["failed_attempts"], if_df[y_col], c=["red" if f else "steelblue" for f in if_df["if_flag"]], edgecolors="black", linewidths=0.5)
   for _, r in if_df.iterrows():
       ax1.annotate(r["ip"], (r["failed_attempts"], r[y_col]), fontsize=6, textcoords="offset points", xytext=(4, 4))
   ax1.scatter([], [], c="red", label="Anomaly")
   ax1.scatter([], [], c="steelblue", label="Normal")
   ax1.set_xlabel("Failed Attempts")
   ax1.set_ylabel(y_label)
   ax1.set_title(f"Isolation Forest — Failed Attempts vs {y_label}")
   ax1.legend()


   # DBSCAN
   for i, cluster in enumerate(sorted(dbscan_df["dbscan_cluster"].unique())):
       mask = dbscan_df["dbscan_cluster"] == cluster
       label = "Outlier" if cluster == -1 else f"Cluster {cluster}"
       color = "red" if cluster == -1 else cluster_colors[i % len(cluster_colors)]
       subset = dbscan_df[mask]
       ax2.scatter(subset["failed_attempts"], subset[y_col], c=color, label=label, edgecolors="black", linewidths=0.5)
       for _, r in subset.iterrows():
           ax2.annotate(r["ip"], (r["failed_attempts"], r[y_col]), fontsize=6, textcoords="offset points", xytext=(4, 4))
   ax2.set_xlabel("Failed Attempts")
   ax2.set_ylabel(y_label)
   ax2.set_title(f"DBSCAN — Failed Attempts vs {y_label}")
   ax2.legend()


plt.tight_layout(h_pad=4)
plt.show()