import streamlit as st
import pandas as pd

# Importing project functions
from parser import parse_log
from features import build_features
from baseline import rule_based_detection
from models import run_isolation_forest, run_dbscan

st.title("SSH Log Anomally Detection")

# For file uploading (capability for user)
uploaded_file = st.file_uploader("Upload auth.log", type=["log"])

if uploaded_file:
        # Reads uploaded files and turns content into lines to be parsed
        df = parse_log(uploaded_file.read().decode("utf-8").splitlines())        

        st.subheader("Raw Log Data")            # Header
        st.write(df)                            # Displays raw parsed data

        features_df = build_features(df)        # Brings features together for display

        st.subheader("Feature Data")
        st.write(features_df)                   # Displaying features

        baseline_df = rule_based_detection(features_df) # Runs rule based detection
        st.subheader("Baseline Results")
        # Displaying only the flagged IPs based on the rule_flag == 1
        st.write(baseline_df[baseline_df["rule_flag"] == 1])

        if_df = run_isolation_forest(features_df)       # Runs IF detection
        st.subheader("Isolation Forest")
        st.write(if_df[if_df["if_flag"] == 1])          # Displaying anomalies flagged by IF

        dbscan_df = run_dbscan(features_df)             # Runs DBSCAN detection
        st.subheader("DBSCAN")
        st.write(dbscan_df[dbscan_df["dbscan_flag"] == 1]) # Displays anomalies flagged by DBSCAN

# Combine all results into one table
combined_df = baseline_df.copy()
combined_df["if_flag"] = if_df["if_flag"]
combined_df["dbscan_flag"] = dbscan_df["dbscan_flag"]

# Agreement scoring
combined_df["agreement"] = (
    combined_df["rule_flag"] +
    combined_df["if_flag"] +
    combined_df["dbscan_flag"]
)

# Display results
st.subheader("Agreement Analysis")

st.write("Strong Attacks (agreement = 3)")
st.write(combined_df[combined_df["agreement"] == 3])

st.write("Likely Attacks (agreement = 2)")
st.write(combined_df[combined_df["agreement"] == 2])