from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from stor.models import Stor
from utils.permissions import IsCustumerPermission

from orders.models import Order
from orders.serializers import OrderSerializer


class OrderRequestView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsCustumerPermission]
    
    def create(self, request, *args, **kwargs):
        stor = get_object_or_404(Stor, id=kwargs.get('pk'))
        
        request.data['stor'] = stor.id
        return super().create(request, *args, **kwargs)
    
class OrderListRetrieveView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def filter_queryset(self, queryset):
        user = self.request.user
        if not user.is_superuser:
            queryset = queryset.filter(user=self.request.user)
        
        return super().filter_queryset(queryset)
    
    def get_object(self):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        
        object = get_object_or_404(Order, **filter_kwargs)

        if object.user.id != self.request.user.id:
            raise PermissionDenied("You don't have permission to access this order")
        
        return object
    
