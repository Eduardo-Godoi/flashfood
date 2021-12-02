from django.shortcuts import get_object_or_404
from products.models import ProductCategory
from products.serializers import ProductSerializer, ProductStorSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from utils.exceptions import Unauthorized
from utils.geolocation import calculate_route, geocoding
from utils.permissions import IsCustumerPermission, IsPartnerPermisson

from .models import Review, Stor, StorCategory
from .serializers import (OwnerStorSerializer, ReviewSerializer,
                          StorCategorySerializer, StorSerializer)


class StorView(ModelViewSet):
    queryset = Stor.objects.all()
    serializer_class = StorSerializer
    permission_classes = [IsAuthenticated, IsPartnerPermisson]
    authentication_classes = [TokenAuthentication]

    def get_serializer(self, *args, **kwargs):
        street = self.request.data.get('street', None)
        district = self.request.data.get('district', None)
        number = self.request.data.get('number', None)
        category = self.request.data.get('category')
        city = self.request.data.get('city', None)
        state = self.request.data.get('state', None)
        cep = self.request.data.get('cep', None)
        coordinates = geocoding(self.request.data)

        if category:
            self.request.data['category'] = {'name': category.title()}

        self.request.data['adress'] = {
            'street': street,
            'district': district,
            'number': number,
            'city': city,
            'state': state,
            'cep': cep,
            'coordinates': coordinates
        }

        return super().get_serializer(*args, **kwargs)

    def list(self, request):
        user = self.request.user

        if 'category' in self.request.GET:
            category = get_object_or_404(StorCategory, name=self.request.GET['category'].title())
            stors = Stor.objects.filter(category_id=category.id)
            serialized = StorSerializer(stors, many=True)
            return Response(serialized.data)

        if user.is_superuser:
            serialized = OwnerStorSerializer(user.stors, many=True)
            return Response(serialized.data)

        stors = Stor.objects.all()
        serialized = StorSerializer(stors, many=True)
        return Response(serialized.data)

    # def filter_queryset(self, queryset):
    #     if 'category' in self.request.GET:
    #         category = get_object_or_404(StorCategory, name=self.request.GET['category'].title())
    #         return queryset.filter(category_id=category.id)
    #     return queryset

    def destroy(self, request, *args, **kwargs):
        user = self.request.user
        stor = self.get_object()

        if user.id is not stor.owner.id:
            raise Unauthorized()

        self.perform_destroy(stor)

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['get'], url_path='products')
    def list_product(self, request,  *args, **kwargs):
        stor = get_object_or_404(Stor, id=kwargs.get('pk'))

        if 'category' in self.request.GET:
            category = ProductCategory.objects.filter(name=self.request.GET['category'])
            products = stor.product.filter(category=category[0].id)

            serialized = ProductStorSerializer(products, many=True)
            return Response(serialized.data)

        serialized = ProductStorSerializer(stor.product, many=True)
        return Response(serialized.data)


class ShowNearbyStores(ModelViewSet):
    queryset = Stor.objects.all()
    serializer_class = StorCategorySerializer

    permission_classes = [IsCustumerPermission]
    authentication_classes = [TokenAuthentication]

    def list(self, queryset):
        customer = self.request.user

        if 'category' in self.request.GET:
            category = get_object_or_404(StorCategory, name=self.request.GET['category'].title())
            list_of_stores = Stor.objects.filter(category_id=category.id)
            stors = calculate_route(customer, list_of_stores)
            return Response(stors)

        categorys = StorCategory.objects.all()
        serialized = StorCategorySerializer(categorys, many=True)
        return Response(serialized.data)


class ReviewView(ModelViewSet):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsCustumerPermission]

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, user=self.request.user)

        self.check_object_permissions(self.request, obj)

        return obj

    def filter_queryset(self, queryset):
        stor = get_object_or_404(Stor, id=self.kwargs["pk"])
        queryset = queryset.filter(stor=stor)

        return super().filter_queryset(queryset)
