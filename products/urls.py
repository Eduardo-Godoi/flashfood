from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import ProductView

router = SimpleRouter()
router.register(prefix=r'product', viewset=ProductView)

urlpatterns = [
    path('<str:stor_id>/', include(router.urls))
]
