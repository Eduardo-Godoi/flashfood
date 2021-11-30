from django.db import models

class Order(models.Model):

    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='orders')
    date = models.DateTimeField()
    total_price = models.FloatField()


class orders_products(models.Model):

    product = models.ForeignKey('products.Product', on_delete=models.PROTECT)
    order = models.ForeignKey('orders.Order', on_delete=models.PROTECT)
    unit_price = models.FloatField()
    quantity = models.IntegerField()
