# System Architecture

The Weather Data Pipeline System is designed as an end-to-end data engineering pipeline.

## Architecture Overview

OpenWeather API
        │
        ▼
API Client
        │
        ▼
ETL Pipeline
        │
        ▼
SQLite Database
        │
        ├── Monitoring (monitor.py)
        ├── Reporting (reporter.py)
        └── Analytics (analysis_report.py)

## Components

### API Client
Fetches weather data from the OpenWeather API.

### ETL Pipeline
Extracts, validates, transforms, and loads data into the SQLite database.

### Database
Stores weather data, city information, and pipeline execution logs.

### Monitoring
Tracks pipeline health and database statistics.

### Reporting
Generates automated reports and alerts.

### Analytics
Creates graphical insights and PDF reports.