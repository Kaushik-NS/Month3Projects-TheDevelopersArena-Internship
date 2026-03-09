import schedule
import time

from etl_pipeline import run_pipeline


def start_scheduler():

    schedule.every(1).minutes.do(run_pipeline)

    print("Scheduler started")

    while True:

        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":

    start_scheduler()