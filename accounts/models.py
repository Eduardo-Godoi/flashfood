from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    adress = models.OneToOneField('accounts.Adress', on_delete=models.CASCADE, related_name='user')

class Adress(models.Model):
    street = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    number = models.IntegerField()