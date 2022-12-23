# Wallet model

from decimal import Decimal

from django.db import models

from zeply_crypto_api.utils.models import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Wallet(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="users"
    )
    label = models.CharField(max_length=50, blank=True)
    balance = models.DecimalField(default=Decimal(0), max_digits=16, decimal_places=8)

    class Meta:
        verbose_name_plural = "wallets"

    def __str__(self):
        return self.user
