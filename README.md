AI-Driven SSH Login Log Anomaly Detection
Overview

This project builds a Python system to detect suspicious SSH login activity from server logs. It parses raw logs, extracts behavioral patterns per IP, and compares rule-based detection with machine learning methods.

Project Structure
AI_481_Project/
│
├── main.py
├── parser.py
├── features.py
├── baseline.py
├── models.py
├── evaluate.py
│
├── data/
│   └── auth.log
│
└── results/
Setup Instructions
1. Clone the repository
git clone https://github.com/YOUR-USERNAME/AI-SSH-Anomaly-Detection.git
cd AI-SSH-Anomaly-Detection
2. Create virtual environment
python3 -m venv venv
3. Activate environment

Mac/Linux:

source venv/bin/activate

Windows:

venv\Scripts\activate
4. Install dependencies
pip install pandas
5. Add log file

Place your SSH log file here:

data/auth.log
6. Run the project
python main.py
Git Workflow

Before working:

git pull

After changes:

git add .
git commit -m "your message"
git push
Team Roles
Steven: Rule-based baseline, integration, report
Citlali: Parser and feature engineering
Quynh: ML models and evaluation
Progress
Completed: parser and feature engineering
Next: rule-based detection
Later: ML models (Isolation Forest, DBSCAN)
AI Component

AI starts in models.py:

Isolation Forest (unsupervised learning)
DBSCAN (clustering)

Everything before that is data preparation, not AI.

Notes
Do not rename files
Keep the structure the same
Always activate venv before running code