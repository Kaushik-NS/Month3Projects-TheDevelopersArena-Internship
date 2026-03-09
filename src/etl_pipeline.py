import logging
from datetime import datetime

from config import CITIES, LOG_FILE
from database import insert_city, insert_weather, create_tables, log_pipeline_run
from api_client import fetch_weather
from validators import validate_weather


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO
)


def run_pipeline():

    logging.info("Pipeline started")
    records = 0

    for city in CITIES:

        try:

            weather = fetch_weather(city)

            if not validate_weather(weather):

                logging.warning(f"Invalid data for {city}")
                continue

            weather["timestamp"] = datetime.now()

            city_id = insert_city(city)

            insert_weather(city_id, weather)

            logging.info(f"Stored weather for {city}")

            log_pipeline_run("SUCCESS", records)

        except Exception as e:

            logging.error(f"Error processing {city}: {e}")

            log_pipeline_run("FAILED", 0)


if __name__ == "__main__":

    create_tables()

    run_pipeline()