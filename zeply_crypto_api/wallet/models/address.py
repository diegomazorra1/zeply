# Address model

from django.db import models

from zeply_crypto_api.utils.models import BaseModel
from .cryptocurrency import CryptoCurrency
from .wallet import Wallet


class Address(BaseModel):
    """
    Model for store addresses.
    """
    value = models.CharField(max_length=50, unique=True)
    cryptocurrency = models.ForeignKey(
        to=CryptoCurrency,
        on_delete=models.CASCADE,
        related_name="addresses",
        related_query_name="address",
    )
    active = models.BooleanField(default=False)
    private_key = models.CharField(max_length=256)

    wallet = models.ForeignKey(Wallet, null=True, related_name="addresses", on_delete=models.CASCADE,)
