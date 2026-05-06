# AI-Driven SSH Login Log Anomaly Detection

My submission for Computer Science Course 481, Artificial Intelligence.

Group Members:

* Quynh Le
* Citlali Garcia
* Steven Solorzano

Language: Python

---

# Project Overview

This project analyzes SSH authentication logs (`auth.log`) to detect suspicious login behavior using both rule-based detection and machine learning.

The system parses raw SSH log files, extracts behavioral features for each IP address, and compares multiple detection methods:

* Rule-Based Baseline
* Isolation Forest
* DBSCAN

The goal is to identify suspicious login activity such as:

* Brute force login attempts
* Rapid failed login attempts
* Multiple username attempts from the same IP
* Unusual login behavior patterns

The project also includes a Streamlit UI for uploading and analyzing log files visually.

---

# Features

* Parses raw SSH authentication logs
* Extracts behavioral features per IP
* Detects suspicious login activity
* Compares AI-based methods against rule-based detection
* Displays results in a Streamlit web interface
* Supports uploaded log file analysis

---

# Technologies Used

* Python
* pandas
* numpy
* scikit-learn
* Streamlit
* matplotlib
* seaborn

---

# Machine Learning Models

## Rule-Based Baseline

Flags suspicious IPs using fixed thresholds such as:

* High failed login count
* High login attempt rate
* Multiple usernames attempted

## Isolation Forest

An unsupervised anomaly detection algorithm that learns what “normal” login behavior looks like and flags statistically unusual behavior.

## DBSCAN

A density-based clustering algorithm that groups similar login behaviors together. Points that do not belong to a cluster are treated as anomalies.

---

# Project Structure

```text
AI_481_Project/
│
├── app.py
├── parser.py
├── features.py
├── baseline.py
├── models.py
├── evaluate.py
├── main.py
│
├── data/
│   └── auth.log
│
├── results/
│
├── venv/
│
└── README.md
```

---

# Setup Instructions

## 1. Clone the Repository

```bash
git clone <repo-url>
cd AI_481_Project
```

---

## 2. Create and Activate Virtual Environment

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install pandas numpy scikit-learn streamlit matplotlib seaborn
```

---

# Running the Project

## Run the Streamlit UI

After activating the virtual environment and installing Streamlit along with all required dependencies, run the command:

```bash
streamlit run app.py
```

The terminal will display a local URL that opens the UI in your browser. If it does not open automatically, copy and paste the URL into your browser manually.

Example:

```text
http://localhost:8501
```

---

# Example Workflow

1. Launch the Streamlit UI
2. Upload an SSH `auth.log` file
3. The system parses the logs
4. Features are extracted for each IP
5. Detection algorithms analyze the data
6. Suspicious IPs and anomalies are displayed

---

# Feature Engineering

The system extracts behavioral features including:

* Failed login count
* Unique usernames attempted
* Attempt duration
* Attempt rate

These features are used by both the rule-based and machine learning models.

---

# Example Detection Logic

## Rule-Based Detection

Flags an IP if:

* Failed attempts exceed a threshold
* Too many usernames are attempted
* Login attempts occur too quickly

## Isolation Forest

* Builds random decision trees
* Detects outliers in login behavior
* Does not require labeled training data

## DBSCAN

* Groups similar behavior patterns into clusters
* Treats isolated points as anomalies

---

# Future Improvements

Potential future improvements include:

* Real-time monitoring
* Live SSH stream analysis
* Additional machine learning models
* Visualization dashboards
* Email or Discord alert system
* Threat intelligence integration
* Geolocation analysis

---

# Datasets

Datasets referenced:

* LogHub OpenSSH logs
* SecRepo auth.log dataset

---

# Notes

* This project is intended for educational and research purposes.
* Machine learning results depend heavily on the quality and diversity of log data.
* Isolation Forest and DBSCAN are both unsupervised learning methods.

---

# Authors

* Steven Solorzano
* Quynh Le
* Citlali Garcia
