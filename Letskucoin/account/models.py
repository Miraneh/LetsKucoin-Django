from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    api_key = models.CharField(max_length=100)
    api_secret = models.CharField(max_length=100)
    api_passphrase = models.CharField(max_length=100)
