from parser import parse_log
from features import build_features
from baseline import rule_based_detection

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
print ("BASELINE RESULT")
print(result_df)
print()

alerts = result_df[result_df["rule_flag"] == 1]
print("SUSPICIOUS IPS")
print(alerts)