# ETL Workflow

This document describes the workflow of the Weather Data Engineering Pipeline.


The system follows a standard ETL architecture.

## Extract
Weather data is fetched from the OpenWeather API.

## Transform
Data validation ensures that temperature, humidity, and pressure values fall within valid ranges.

Invalid records are skipped.

## Load
Validated records are stored in the SQLite database.

## Pipeline Workflow Path

OpenWeather API
      │
      ▼
API Request (api_client.py)
      │
      ▼
Data Extraction
      │
      ▼
Validation Layer (validators.py)
      │
      ▼
Data Transformation
      │
      ▼
ETL Pipeline Execution (etl_pipeline.py)
      │
      ▼
Database Storage (SQLite)
      │
      ▼
weather_data Table
      │
      ▼
Monitoring (monitor.py)
      │
      ▼
Report Generation (reporter.py)
      │
      ▼
Analytics & Visualization (analysis_report.py)
      │
      ▼
Generated Reports (reports/)