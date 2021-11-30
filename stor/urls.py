from rest_framework.routers import SimpleRouter

from .views import StorView

router = SimpleRouter()
router.register(prefix=r'stor', viewset=StorView)

urlpatterns = router.urls

print(urlpatterns)
