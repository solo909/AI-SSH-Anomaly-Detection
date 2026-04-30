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

        df = parse_log(uploaded_file)           # Runs parse on uploaded file

        st.subheader("Raw Log Data")            # Header
        st.write(df)                            # Displays raw parsed data

        featrues_df = build_features(df)        # Brings features together for display

        st.subheader("Feature Data")
        st.write(featrues_df)                   # Displaying features

        