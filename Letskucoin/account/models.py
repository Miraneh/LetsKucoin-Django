from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    api_key = models.CharField(max_length=100)
    api_secret = models.CharField(max_length=100)
    api_passphrase = models.CharField(max_length=100)


class Position(models.Model):
    objects = models.Manager()
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    id = models.CharField(max_length=100)
    currency = models.CharField(max_length=10)
    account_type = models.CharField(max_length=10)
    balance = models.FloatField()
    available = models.FloatField()
    holds = models.FloatField()


