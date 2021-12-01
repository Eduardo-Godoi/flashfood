from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import GenericViewSet
from utils.permissions import IsPartnerPermisson

from .models import Product
from .serializer import ProductSerializer


class ProductView(mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  GenericViewSet,
                  ):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsPartnerPermisson]

    def get_serializer(self, *args, **kwargs):
        category = self.request.data.get('category')
        self.request.data['category'] = {'name': category.title()}

        return super().get_serializer(*args, **kwargs)
