import sqlite3
from config import DB_NAME
from datetime import datetime
import pytz


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cities (
        city_id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_name TEXT UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather_data (
        record_id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_id INTEGER,
        timestamp DATETIME,
        temperature REAL,
        humidity INTEGER,
        pressure REAL,
        wind_speed REAL,
        condition TEXT,
        FOREIGN KEY(city_id) REFERENCES cities(city_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pipeline_logs (
        log_id INTEGER PRIMARY KEY AUTOINCREMENT,
        log_time DATETIME DEFAULT CURRENT_TIMESTAMP,
        message TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pipeline_runs (
        run_id INTEGER PRIMARY KEY AUTOINCREMENT,
        run_time DATETIME DEFAULT CURRENT_TIMESTAMP,
        status TEXT,
        records_processed INTEGER
    )
    """)

    conn.commit()
    conn.close()


def insert_city(city):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT OR IGNORE INTO cities(city_name) VALUES(?)",
        (city,)
    )

    conn.commit()

    cursor.execute(
        "SELECT city_id FROM cities WHERE city_name=?",
        (city,)
    )

    city_id = cursor.fetchone()[0]

    conn.close()

    return city_id


def insert_weather(city_id, weather):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO weather_data
    (city_id, timestamp, temperature, humidity, pressure, wind_speed, condition)
    VALUES (?,?,?,?,?,?,?)
    """, (
        city_id,
        weather["timestamp"],
        weather["temperature"],
        weather["humidity"],
        weather["pressure"],
        weather["wind_speed"],
        weather["condition"]
    ))
    
    conn.commit()
    conn.close()


def log_pipeline_run(status, records):

    conn = get_connection()
    cursor = conn.cursor()

    ist = pytz.timezone("Asia/Kolkata")
    now_ist = datetime.now(ist)

    cursor.execute("""
    INSERT INTO pipeline_runs (run_time, status, records_processed)
    VALUES (?,?,?)
    """, (now_ist, status, records))

    conn.commit()
    conn.close()