from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import ReviewView, ShowNearbyStores, StorView

router = SimpleRouter()
router.register(prefix=r'stor', viewset=StorView)
router.register(prefix=r'category', viewset=ShowNearbyStores)

urlpatterns = [
    path('', include(router.urls)),
    path('stor/<str:pk>/review/', ReviewView.as_view({
        'post': 'create',
        'put': 'update',
        'delete': 'destroy',
        'get': 'list'
        }))
]

urlpatterns += router.urls
