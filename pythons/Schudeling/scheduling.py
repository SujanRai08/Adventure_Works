# Applications in Data Engineering
# Automate workflows.
# Process large datasets efficiently.
# Build resilient ETL pipelines.
# Integrate multiple data sources.

import schedule
import time

def job():
    print("Task executed!")

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

# pip install apache-airflow