import streamlit as st
import pandas as pd

# Importing project functions
from parser import parse_log
from features import build_features
from baseline import rule_based_detection
from models import run_isolation_forest, run_dbscan

st.title("SSH Log Anomally Detection")