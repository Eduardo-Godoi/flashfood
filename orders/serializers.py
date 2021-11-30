from rest_framework import serializers

from orders.models import Order, orders_products
from products.serializers import ProductSerializer
from accounts.serializers import UserSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    user = UserSerializer()
    class Meta:
        model = Order
        fields = ['id', 'product', 'user', 'date', 'total_price']
        depth = 1


class OrderProduct(serializers.ModelSerializer):
    product = ProductSerializer()
    order = OrderSerializer()
    class Meta:
        model = orders_products
        fields = ['__all__']
        depth = 1
