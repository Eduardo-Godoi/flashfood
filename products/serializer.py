from django.db import models
from rest_framework import serializers
from .models import Product, ProductCategory
from accounts.models import User
from stor.serializers import StorSerializer


class ProductCategorySerializer(serializers.Serializer):
    name = models.CharField()


class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()

    class Meta:
        model = Product
        fields = ["name", "price", "category"]

    def create(self, validated_data):
        view_kwarg = self.context["view"].kwargs
        owner = User.objects.get(id=self.context["request"].user.id)
        stor = owner.stors.filter(id=view_kwarg["stor_id"]).first()
        print(validated_data)
        category_data = validated_data.pop("category")
        # lançar exceção caso a stor não pertencer ao owner

        category = ProductCategory.objects.get_or_create(**category_data)[0]
        validated_data["stor"] = stor
        validated_data["category"] = category
        return super().create(validated_data)
