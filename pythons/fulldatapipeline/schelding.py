# using schedule for automation 
import schedule
import time

def job():
    print('pipeline running')

schedule.every().day.at('10:00').do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

# Using Crontab for Scheduling 
# 0 10 * * * /usr/bin/python3 /path/to/pipeline.py 
