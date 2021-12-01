from accounts.models import User
from rest_framework import serializers
from rest_framework.exceptions import NotFound
from stor.models import Stor

from .models import Product, ProductCategory


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()

    class Meta:
        model = Product
        fields = ["id", "name", "price", "category"]

    def create(self, validated_data):
        owner = User.objects.get(id=self.context["request"].user.id)
        stor_id = self.context["view"].kwargs.get("stor_id")
        stor = owner.stors.filter(id=stor_id).first()
        if not stor:
            raise NotFound

        category_data = validated_data.pop("category")
        category, _ = ProductCategory.objects.get_or_create(**category_data)

        product = Product.objects.create(
            **validated_data, stor=stor, category=category
            )

        return product

    def update(self, instance, validated_data):
        store_id = self.context["view"].kwargs.get("stor_id")
        product_id = self.context["view"].kwargs.get("pk")
        category_data = validated_data.pop("category")

        stor = Stor.objects.filter(id=store_id).first()
        if not stor:
            raise NotFound

        category, _ = ProductCategory.objects.get_or_create(
            name=category_data["name"]
            )
        product = stor.product.filter(id=product_id).first()
        if not product:
            raise NotFound

        product.category = category

        return super().update(product, validated_data)
