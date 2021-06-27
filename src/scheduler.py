import os
from datetime import datetime
from SharedLibrary.env_utils import load_parameters
from SharedLibrary.mongo_utils import access_collection, delete_invalid_users

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

SCHEDULER = BlockingScheduler()
HOUR = os.getenv('SCHEDULE_TIME_HOUR')
MONGO_PARAMETERS = load_parameters()


@SCHEDULER.scheduled_job(IntervalTrigger(hours=HOUR))
def users_cron():
    failed, collection = access_collection(MONGO_PARAMETERS)
    if failed:
        raise Exception("Failed while trying to connect to mongo")
    delete_invalid_users(collection)
    print('dask train_model! The time is: %s' % datetime.now())


SCHEDULER.start()
