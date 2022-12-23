from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from zeply_crypto_api.users.api.views import UserViewSet
from zeply_crypto_api.wallet.views import AddressViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("address", AddressViewSet)


app_name = "api"
urlpatterns = router.urls
