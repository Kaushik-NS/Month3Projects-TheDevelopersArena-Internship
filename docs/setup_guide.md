# Setup Instructions

## 1 Install Python
Ensure Python 3.9+ is installed.

## 2 Install Dependencies

pip install -r requirements.txt

## 3 Configure API Key

Edit config.py and insert your OpenWeather API key.

API_KEY = "YOUR_API_KEY"

## 4 Initialize Database

python etl_pipeline.py

## 5 Run Scheduler

python scheduler.py

## 6 Monitor Pipeline

python monitor.py

## 7 Generate Analytics Report

python analysis_report.py