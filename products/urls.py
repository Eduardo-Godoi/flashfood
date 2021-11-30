from django.urls import path
from .views import ProductView

urlpatterns = [
    path('<stor_id>/product/', ProductView.as_view({'post': 'create'})),
]
