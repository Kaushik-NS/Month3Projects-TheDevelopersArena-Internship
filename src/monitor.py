import sqlite3
from config import DB_NAME


def health_check():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM weather_data")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM cities")
    cities = cursor.fetchone()[0]

    conn.close()

    print("\nPIPELINE HEALTH REPORT")
    print("----------------------")
    print(f"Total records: {total}")
    print(f"Cities tracked: {cities}")


if __name__ == "__main__":
    health_check()