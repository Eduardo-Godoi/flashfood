from accounts.models import Adress
from accounts.serializers import AdressSerializer, UserSerializer
from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.fields import IntegerField

from .models import Review, Stor, StorCategory
from utils.exceptions import UnprocessableEntity, BadRequest


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
        fields = ['id', 'name', 'category', 'owner', 'adress']

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

        instance_stor = get_object_or_404(Stor, id=instance.id)

        category, _ = StorCategory.objects.get_or_create(**category_data)
        category.stors.add(instance_stor)

        return super().update(instance_stor, validated_data)


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    stars = IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )

    class Meta:
        model = Review
        fields = ["id", "stars", "review", "user"]

    def create(self, validated_data):
        stor_id = self.context['view'].kwargs["pk"]
        stor = get_object_or_404(Stor, id=stor_id)
        user = self.context["request"].user
        if user.orders.count() == 0:
            raise BadRequest

        validated_data["user"] = user
        validated_data["stor"] = stor

        return super().create(validated_data)

    def validate(self, attrs):
        store_id = self.context['view'].kwargs["pk"]
        user = self.context["request"].user
        stor = get_object_or_404(Stor, id=store_id)
        http_method = self.context["request"].method

        has_review = stor.reviews.filter(user=user).first()

        if has_review and http_method == "POST":
            raise UnprocessableEntity()

        return super().validate(attrs)
