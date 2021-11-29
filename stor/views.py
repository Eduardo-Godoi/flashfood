from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Stor, StorCategory
from .serializers import StorSerializer, StorCategorySerializer


class StorView(ModelViewSet):
    queryset = Stor.objects.all()
    serializer_class = StorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def get_serializer(self, *args, **kwargs):
        street = self.request.data.get('street', None)
        district = self.request.data.get('district', None)
        number = self.request.data.get('number', None)
        category = self.request.data.get('category')

        if category:
            self.request.data['category'] = {'name': category.title()}

        self.request.data['adress'] = {
            'street': street,
            'district': district,
            'number': number
        }

        return super().get_serializer(*args, **kwargs)

    def filter_queryset(self, queryset):
        if 'category' in self.request.GET:
            category = get_object_or_404(StorCategory, name=self.request.GET['category'].title())
            return queryset.filter(category_id=category.id)
        return queryset


    @action(detail=True, methods=['get'], url_path='products')
    def list_product(self, request,  *args, **kwargs):
        if 'category' in self.request.GET:
            stor = get_object_or_404(Stor, id=kwargs.get('pk'))
            return stor.products.filter(name__contains=self.request.GET['category'])
        serialized = ProductSerializer(stor.products, many=True)
        return Response(serialized.data)
