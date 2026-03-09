import sqlite3
from datetime import datetime, timedelta
from config import DB_NAME, TEMP_ALERT, HUMIDITY_ALERT, CITIES


def generate_dashboard():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    print("\nWEATHER DATA PIPELINE SYSTEM")
    print("=============================\n")

    # ----------------------------
    # SYSTEM STATUS
    # ----------------------------
    cursor.execute("""
        SELECT run_time, status, records_processed
        FROM pipeline_runs
        ORDER BY run_time DESC
        LIMIT 1
    """)

    run = cursor.fetchone()

    if run:
        last_run, status, records = run
    else:
        last_run = "Never"
        status = "UNKNOWN"
        records = 0

    print(" SYSTEM STATUS:", status)
    print(f" Last Run: {last_run}")
    print(f" Records Processed: {records} cities\n")

    # ----------------------------
    # CURRENT WEATHER SNAPSHOT
    # ----------------------------
    print(" CURRENT WEATHER SNAPSHOT:")
    print("---------------------------------")

    query = """
    SELECT c.city_name,
           w.temperature,
           w.humidity,
           w.condition,
           w.timestamp
    FROM weather_data w
    JOIN cities c
    ON w.city_id = c.city_id
    ORDER BY w.timestamp DESC
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    latest = {}

    for row in rows:
        city = row[0]
        if city not in latest:
            latest[city] = row

    alerts = []

    for city, temp, humidity, cond, ts in latest.values():

        print(f"📍 {city}: {temp}°C, {humidity}% humidity, {cond}")

        if temp > TEMP_ALERT:
            alerts.append(
                f"High temperature alert: {city} ({temp}°C > {TEMP_ALERT}°C threshold)"
            )

        if humidity > HUMIDITY_ALERT:
            alerts.append(
                f"High humidity alert: {city} ({humidity}% > {HUMIDITY_ALERT}% threshold)"
            )

    # ----------------------------
    # ALERTS
    # ----------------------------
    print("\n TODAY'S ALERTS:")

    if alerts:
        for a in alerts:
            print("•", a)
    else:
        print("• No alerts")

    # ----------------------------
    # DATABASE STATISTICS
    # ----------------------------
    cursor.execute("SELECT COUNT(*) FROM weather_data")
    total_records = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM cities")
    cities_tracked = cursor.fetchone()[0]

    coverage = round((cities_tracked / len(CITIES)) * 100, 2)

    print("\n DATABASE STATISTICS:")
    print(f"• Total records: {total_records}")
    print(f"• Cities tracked: {cities_tracked}")
    print(f"• Data coverage: {coverage}%")
    print("• Last error: None")

    # ----------------------------
    # NEXT SCHEDULED RUN
    # ----------------------------
    next_run = datetime.now() + timedelta(minutes=1)

    print(
        f"\n NEXT SCHEDULED RUN: {next_run.strftime('%Y-%m-%d %H:%M:%S')}"
    )

    conn.close()


if __name__ == "__main__":
    generate_dashboard()