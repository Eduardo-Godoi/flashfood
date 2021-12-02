from datetime import datetime

from django.core.exceptions import ValidationError
from products.models import Product
from rest_framework import serializers
from stor.models import Stor

from orders.models import Order, OrderProduct


class OrderProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderProduct
        fields = ['product', 'unit_price', 'quantity']

class OrderProductRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class OrderSerializer(serializers.ModelSerializer):
    stor = serializers.PrimaryKeyRelatedField(queryset=Stor.objects.all(), write_only=True)
    products = OrderProductRequestSerializer(many=True, write_only=True)
    order_products = OrderProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "order_products", "date", "total_price", "products", "stor"]
        
        extra_kwargs = {
            'total_price': {'read_only': True},
            'user': {'read_only': True},
            'date': {'read_only': True}
        }

    def create(self, validated_data):
        total_price = 0
        date = datetime.utcnow()
        
        products_request = validated_data['products']
        products = []
        for p in products_request:
            product = Product.objects.get(id=p['id'])
            
            total_price += product.price * p['quantity']
            products.append((product, p['quantity']))
            
        order = Order.objects.create(total_price=total_price, user=self.context['request'].user, date=date)
        
        for p, quantity in products:
            order.products.add(p, through_defaults={'unit_price': p.price, 'quantity': quantity})
            
        return order

    def validate(self, attrs):
        stor = attrs['stor']
        products = attrs['products']
        
        for p in products:
            try:
                product = Product.objects.get(id=p['id'])
            except Product.DoesNotExist:
                raise ValidationError('Product does not exist.')
            if product.stor.id != stor.id:
                raise ValidationError('Product not in stor.')
                
        return super().validate(attrs)

