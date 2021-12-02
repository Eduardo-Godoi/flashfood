from django.urls import path, include
from rest_framework.routers import SimpleRouter

from orders.views import OrderRequestView, OrderListRetrieveView

router = SimpleRouter()
router.register(prefix=r'orders', viewset=OrderListRetrieveView, basename='order')

urlpatterns = [
    path('stor/', include(router.urls)),
    path('stor/<int:pk>/orders/', OrderRequestView.as_view()),
]
