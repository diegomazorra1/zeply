from django.db import models

from zeply_crypto_api.utils.models import BaseModel


class CryptoCurrency(BaseModel):
    name = models.CharField(max_length=100, unique=True, )

    class Meta:
        verbose_name_plural = "cryptocurrencies"

    def __str__(self):
        return self.name
