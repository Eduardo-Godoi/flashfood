from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import StorView, ReviewView

router = SimpleRouter()
router.register(prefix=r'stor', viewset=StorView)

urlpatterns = [
    path('', include(router.urls)),
    path('stor/<str:pk>/review/', ReviewView.as_view({
        'post': 'create',
        'put': 'update',
        'delete': 'destroy',
        'get': 'list'
        }))
]
