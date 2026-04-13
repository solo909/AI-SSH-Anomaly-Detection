from parser import parse_log
from features import build_features

file_path = "data/auth.log"

df = parse_log(file_path)
print("RAW LOG DATA")
print(df)
print()

features_df = build_features(df)
print("FEATURE DATA")
print(features_df)
print()
print("Total IPs:", len(features_df))