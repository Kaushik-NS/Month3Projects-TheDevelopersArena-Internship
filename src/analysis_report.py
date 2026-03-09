import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from config import DB_NAME

# -----------------------------------
# Setup report directory
# -----------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = os.path.join(BASE_DIR, "reports")

if not os.path.exists(REPORT_DIR):
    os.makedirs(REPORT_DIR)

# Current date for report
report_date = datetime.now().strftime("%Y-%m-%d")

conn = sqlite3.connect(DB_NAME)

# -----------------------------------
# 1 Highest Average Temperature City
# -----------------------------------
query = """
SELECT c.city_name, AVG(w.temperature) AS avg_temp
FROM weather_data w
JOIN cities c ON w.city_id = c.city_id
GROUP BY c.city_name
"""

df = pd.read_sql(query, conn)

plt.figure()
df.plot(x="city_name", y="avg_temp", kind="bar", legend=False)
plt.title("Average Temperature by City")
plt.ylabel("Temperature (°C)")
plt.tight_layout()

avg_temp_chart = os.path.join(REPORT_DIR, f"avg_temp_city_{report_date}.png")
plt.savefig(avg_temp_chart)
plt.close()

# -----------------------------------
# 2 Temperature Trend (Last 30 Days)
# -----------------------------------
query = """
SELECT DATE(timestamp) as day, AVG(temperature) as avg_temp
FROM weather_data
WHERE timestamp >= DATE('now','-30 day')
GROUP BY day
ORDER BY day
"""

df = pd.read_sql(query, conn)

plt.figure()
plt.plot(df["day"], df["avg_temp"])
plt.xticks(rotation=45)
plt.title("Temperature Trend (Last 30 Days)")
plt.ylabel("Temperature °C")
plt.tight_layout()

trend_chart = os.path.join(REPORT_DIR, f"temp_trend_{report_date}.png")
plt.savefig(trend_chart)
plt.close()

# -----------------------------------
# 3 Humidity vs Rainfall
# -----------------------------------
query = """
SELECT
CASE
WHEN condition LIKE '%rain%' THEN 'Rain'
ELSE 'No Rain'
END as rainfall,
AVG(humidity) as avg_humidity
FROM weather_data
GROUP BY rainfall
"""

df = pd.read_sql(query, conn)

plt.figure()
df.plot(x="rainfall", y="avg_humidity", kind="bar", legend=False)
plt.title("Humidity vs Rainfall")
plt.ylabel("Humidity %")
plt.tight_layout()

humidity_chart = os.path.join(REPORT_DIR, f"humidity_rain_{report_date}.png")
plt.savefig(humidity_chart)
plt.close()

# -----------------------------------
# 4 Seasonal Extreme Temperatures
# -----------------------------------
query = """
SELECT
CASE
WHEN strftime('%m', timestamp) IN ('03','04','05') THEN 'Summer'
WHEN strftime('%m', timestamp) IN ('06','07','08','09') THEN 'Monsoon'
WHEN strftime('%m', timestamp) IN ('10','11') THEN 'Post-Monsoon'
ELSE 'Winter'
END as season,
MAX(temperature) as max_temp
FROM weather_data
GROUP BY season
"""

df = pd.read_sql(query, conn)

plt.figure()
df.plot(x="season", y="max_temp", kind="bar", legend=False)
plt.title("Seasonal Extreme Temperatures")
plt.ylabel("Temperature °C")
plt.tight_layout()

season_chart = os.path.join(REPORT_DIR, f"season_temp_{report_date}.png")
plt.savefig(season_chart)
plt.close()

# -----------------------------------
# 5 Peak Temperature Hours
# -----------------------------------
query = """
SELECT
strftime('%H', timestamp) as hour,
AVG(temperature) as avg_temp
FROM weather_data
GROUP BY hour
ORDER BY hour
"""

df = pd.read_sql(query, conn)

plt.figure()
plt.plot(df["hour"], df["avg_temp"])
plt.title("Peak Temperature Hours")
plt.xlabel("Hour of Day")
plt.ylabel("Temperature °C")
plt.tight_layout()

peak_chart = os.path.join(REPORT_DIR, f"peak_hour_{report_date}.png")
plt.savefig(peak_chart)
plt.close()

conn.close()

# -----------------------------------
# Generate PDF Report
# -----------------------------------
styles = getSampleStyleSheet()

pdf_path = os.path.join(
    REPORT_DIR,
    f"weather_analysis_report_{report_date}.pdf"
)

report = SimpleDocTemplate(pdf_path)

elements = []

elements.append(
    Paragraph(
        f"Weather Data Analysis Report - {report_date}",
        styles['Title']
    )
)

elements.append(Spacer(1, 20))

charts = [
    avg_temp_chart,
    trend_chart,
    humidity_chart,
    season_chart,
    peak_chart
]

for chart in charts:
    elements.append(Image(chart, width=500, height=300))
    elements.append(Spacer(1, 20))

report.build(elements)

print(f"\nReport generated successfully:")
print(pdf_path)