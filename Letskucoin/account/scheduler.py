import sys

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django.utils import timezone
from .models import User, Position
from kucoin.client import User as U


def check_information():
    users = User.objects.all()
    print("Checking information....")
    for user in users:
        try:
            client = U(user.api_key, user.api_secret, user.api_passphrase)
            resp = client.get_account_list()[0]
            print(resp)
            Position.objects.create(kucoin_id=resp['id'], user_id=user.id, currency=resp['currency'],
                                    account_type=resp['type'],
                                    balance=resp['balance'], available=resp['available'], holds=resp['holds'])

        except Exception as e:
            print(e)


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    scheduler.add_job(check_information, 'interval', minutes=1, name='check_info', jobstore='default')
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)
