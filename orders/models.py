from django.db import models

class Order(models.Model):

    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField('products.Product', through='orders.OrderProduct')
    date = models.DateTimeField()
    total_price = models.FloatField(default=0)


class OrderProduct(models.Model):

    product = models.ForeignKey('products.Product', on_delete=models.PROTECT)
    order = models.ForeignKey('orders.Order', on_delete=models.PROTECT, related_name='order_products')
    unit_price = models.FloatField()
    quantity = models.IntegerField()
