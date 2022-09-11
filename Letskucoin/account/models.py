from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    api_key = models.CharField(max_length=100)
    api_secret = models.CharField(max_length=100)
    api_passphrase = models.CharField(max_length=100)


class Position(models.Model):
    objects = models.Manager()
    kucoin_id = models.CharField(max_length=100)
    user_id = models.IntegerField()
    currency = models.CharField(max_length=10)
    account_type = models.CharField(max_length=10)
    balance = models.FloatField()
    available = models.FloatField()
    holds = models.FloatField()


