from django.db import models
from django.db.models.deletion import CASCADE


class Stor(models.Model):
    name = models.CharField(max_length=255)
    adress = models.OneToOneField('accounts.Adress', on_delete=models.CASCADE, related_name='stor')
    owner = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='stors')
    category = models.ForeignKey('stor.StorCategory', on_delete=models.CASCADE, related_name='stors')


class StorCategory(models.Model):
    name = models.CharField(max_length=255)


class Review(models.Model):
    stars = models.IntegerField()
    review = models.TextField()

    user = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE, related_name='review'
        )
    stor = models.ForeignKey(
        'stor.Stor', on_delete=CASCADE, related_name='reviews'
        )
