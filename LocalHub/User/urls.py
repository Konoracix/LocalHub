from rest_framework.routers import DefaultRouter
from User.views import UserViewSet

router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = router.urls