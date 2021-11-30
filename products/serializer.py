from django.shortcuts import get_object_or_404
from django.db import models
from rest_framework import serializers
from .models import Product, ProductCategory
from stor.models import Stor


class ProductCategorySerializer(serializers.Serializer):
    name = models.CharField()


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
        

    def create(self, validated_data):
        view_kwarg = self.context["view"].kwargs
        stor = get_object_or_404(Stor, id=view_kwarg["pk"])

        category = ProductCategory.objects.get_or_create(
            name=validated_data.pop("category")
            )

        validated_data["stor_id"] = stor.id
        validated_data["category_id"] = category.id
        return super().create(validated_data)
