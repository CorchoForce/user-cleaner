import os
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

scheduler = BlockingScheduler()
hour = os.getenv('SCHEDULE_TIME_HOUR')


@scheduler.scheduled_job(IntervalTrigger(hours=hour))
def delete_invalid_users():
    print('dask train_model! The time is: %s' % datetime.now())


scheduler.start()
