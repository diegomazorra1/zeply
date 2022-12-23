"""Wallet URLs."""

from rest_framework.routers import DefaultRouter
from zeply_crypto_api.wallet import views

app_name = 'wallet'

router = DefaultRouter()
router.register('wallet', views.AddressViewSet, basename='wallet')
