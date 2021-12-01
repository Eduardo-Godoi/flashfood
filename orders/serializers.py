from rest_framework import serializers

from orders.models import Order, orders_products
from products.serializers import ProductSerializer
from accounts.serializers import UserSerializer
from products.models import Product


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    user = UserSerializer()
    class Meta:
        model = Order
        fields = ['id', 'product', 'user', 'date', 'total_price']
        depth = 1

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        products_data = validated_data.pop('product')
        order = Order.objects.create(**validated_data)

        for product_data in products_data:
            product, _ = Product.objects.get_or_create(name=product_data['name'])
            order.product.add(product)

        order.user.add(user_data)

        return order


class OrderProduct(serializers.ModelSerializer):
    product = ProductSerializer()
    order = OrderSerializer()
    class Meta:
        model = orders_products
        fields = ['__all__']
        depth = 1
