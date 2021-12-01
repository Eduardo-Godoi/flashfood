from rest_framework.routers import SimpleRouter

from .views import StorView, ShowNearbyStores

router = SimpleRouter()
router.register(prefix=r'stor', viewset=StorView)
router.register(prefix=r'category', viewset=ShowNearbyStores)

urlpatterns = router.urls

print(urlpatterns)
