from apscheduler.schedulers.background import BackgroundScheduler
from positions_api import check_information


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_information(), 'interval', minutes=1)
    scheduler.start()
