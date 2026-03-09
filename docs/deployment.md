WEATHER DATA PIPELINE SYSTEM
DEPLOYMENT INSTRUCTIONS
==================================================

This document explains how to deploy and run the Weather Data Engineering Pipeline.

The system performs the following tasks:
- Fetches weather data from the OpenWeather API
- Validates and transforms the data
- Stores the data in an SQLite database
- Runs automatically using a scheduler
- Generates monitoring reports and analytics reports


--------------------------------------------------
1. INSTALL PYTHON DEPENDENCIES
--------------------------------------------------

Install the required Python libraries using the requirements file.

Command:

pip install -r requirements.txt

Required libraries include:

- requests
- pandas
- matplotlib
- schedule
- reportlab
- pytz


--------------------------------------------------
2. CONFIGURE OPENWEATHER API KEY
--------------------------------------------------

Open the file:

config.py

Insert your OpenWeather API key.

Example:

API_KEY = "YOUR_API_KEY"

Also verify the cities list and other configuration parameters.


--------------------------------------------------
3. INITIALIZE DATABASE (FIRST RUN ONLY)
--------------------------------------------------

The database must be initialized before running the scheduler.

Run the ETL pipeline once to create database tables.

Command:

python etl_pipeline.py


This step will create the SQLite database:

weather_data.db

And the following tables:

- cities
- weather_data
- pipeline_runs
- pipeline_logs


--------------------------------------------------
4. START THE AUTOMATED PIPELINE
--------------------------------------------------

Run the scheduler to start automated weather data collection.

Command:

python scheduler.py

The scheduler will run the ETL pipeline periodically and store
new weather records in the database.


--------------------------------------------------
5. MONITOR PIPELINE STATUS
--------------------------------------------------

You can check the health of the pipeline using the monitoring script.

Command:

python monitor.py


Example Output:

PIPELINE HEALTH REPORT
----------------------
Total records: 1213
Cities tracked: 5


--------------------------------------------------
6. GENERATE ANALYTICS REPORTS
--------------------------------------------------

To generate graphical analytics reports and PDF summaries, run:

Command:

python analysis_report.py


Generated reports will be saved in the folder:

reports/


Example:

reports/weather_analysis_report_2026-03-09.pdf


--------------------------------------------------
7. CHECK DATABASE MANUALLY (OPTIONAL)
--------------------------------------------------

To inspect the database manually using SQLite:

Command:

sqlite3 weather_data.db


List tables:

.tables


View weather records:

SELECT * FROM weather_data LIMIT 10;


--------------------------------------------------
DEPLOYMENT WORKFLOW
--------------------------------------------------

Install dependencies
        ↓
Configure API key
        ↓
Initialize database
        ↓
Start scheduler
        ↓
Monitor pipeline
        ↓
Generate reports


--------------------------------------------------
SYSTEM OUTPUT
--------------------------------------------------

Logs are stored in:

logs/pipeline.log

Analytics reports are stored in:

reports/

Database file:

weather_data.db


End of Deployment Instructions
==================================================