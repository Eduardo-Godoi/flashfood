from django.urls import path

from orders.views import OrderView


urlpatterns = [
    path('orders/', OrderView.as_view()),
    path('orders/<int:pk>', OrderView.as_view()),
]
