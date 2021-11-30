from django.db import models


class Stor(models.Model):
    name = models.CharField(max_length=255)
    adress = models.OneToOneField('accounts.Adress', on_delete=models.CASCADE, related_name='stor')
    owner = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='stors')
    category = models.ForeignKey('stor.StorCategory', on_delete=models.CASCADE, related_name='stors')


class StorCategory(models.Model):
    name = models.CharField(max_length=255)
