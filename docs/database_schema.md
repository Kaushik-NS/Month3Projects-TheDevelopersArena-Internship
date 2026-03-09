DATABASE SCHEMA
===============

Database Name: weather_data.db

The weather data pipeline uses an SQLite database to store city information,
weather observations, pipeline execution records, and system logs.

The database contains the following tables:

1. cities
2. weather_data
3. pipeline_runs
4. pipeline_logs


------------------------------------------------------------
TABLE: cities
------------------------------------------------------------

Description:
Stores the list of cities monitored by the weather pipeline.

Columns:

city_id
Type: INTEGER
Description: Primary key (auto-increment)

city_name
Type: TEXT
Description: Name of the city

created_at
Type: TIMESTAMP
Description: Timestamp when the city record was created


SQL Definition:

CREATE TABLE cities (
    city_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_name TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


------------------------------------------------------------
TABLE: weather_data
------------------------------------------------------------

Description:
Stores weather observations retrieved from the OpenWeather API.

Columns:

record_id
Type: INTEGER
Description: Primary key

city_id
Type: INTEGER
Description: Foreign key referencing cities.city_id

timestamp
Type: DATETIME
Description: Time when the weather data was recorded

temperature
Type: REAL
Description: Temperature in Celsius

humidity
Type: INTEGER
Description: Humidity percentage

pressure
Type: REAL
Description: Atmospheric pressure

wind_speed
Type: REAL
Description: Wind speed

condition
Type: TEXT
Description: Weather condition description


SQL Definition:

CREATE TABLE weather_data (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_id INTEGER,
    timestamp DATETIME,
    temperature REAL,
    humidity INTEGER,
    pressure REAL,
    wind_speed REAL,
    condition TEXT,
    FOREIGN KEY(city_id) REFERENCES cities(city_id)
);


------------------------------------------------------------
TABLE: pipeline_runs
------------------------------------------------------------

Description:
Tracks the execution status of the ETL pipeline.

Columns:

run_id
Type: INTEGER
Description: Primary key

run_time
Type: DATETIME
Description: Timestamp of pipeline execution

status
Type: TEXT
Description: Execution status (SUCCESS or FAILED)

records_processed
Type: INTEGER
Description: Number of records processed during the run


SQL Definition:

CREATE TABLE pipeline_runs (
    run_id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    status TEXT,
    records_processed INTEGER
);


------------------------------------------------------------
TABLE: pipeline_logs
------------------------------------------------------------

Description:
Stores system log messages generated during pipeline execution.

Columns:

log_id
Type: INTEGER
Description: Primary key

log_time
Type: DATETIME
Description: Timestamp of log message

message
Type: TEXT
Description: Log message


SQL Definition:

CREATE TABLE pipeline_logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    log_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    message TEXT
);


------------------------------------------------------------
SUMMARY
------------------------------------------------------------

cities
    Stores the list of monitored cities.

weather_data
    Stores weather observations collected from the API.

pipeline_runs
    Tracks pipeline execution results.

pipeline_logs
    Stores operational logs generated during pipeline execution.