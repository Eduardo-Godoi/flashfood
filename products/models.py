from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=255)
    price = models.FloatField()

    category = models.ForeignKey(
        'products.ProductCategory',
        on_delete=models.PROTECT,
        related_name='product'
        )
    stor = models.ForeignKey(
        "stor.Stor",
        on_delete=models.CASCADE,
        related_name='product'
        )


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
