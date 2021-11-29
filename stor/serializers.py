from accounts.models import Adress
from accounts.serializers import AdressSerializer, UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import Stor, StorCategory


class StorCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StorCategory
        fields = '__all__'
        depth = 1


class StorSerializer(serializers.ModelSerializer):
    adress = AdressSerializer()
    category = StorCategorySerializer()
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Stor
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        adress_data = validated_data.pop('adress')
        category_data = validated_data.pop('category')

        category, _ = StorCategory.objects.get_or_create(**category_data)
        adress = Adress.objects.create(**adress_data)
        stor = Stor.objects.create(**validated_data, adress=adress, owner=user, category=category)

        return stor

    def update(self, instance, validated_data):
        adress_data = validated_data.pop('adress')
        category_data = validated_data.pop('category')

        instace_adress = get_object_or_404(Adress, id=instance.adress.id)
        super().update(instace_adress, adress_data)

        category, _ = StorCategory.objects.get_or_create(**category_data)
        category.stors.add(instance)
        return super().update(instance, validated_data)
