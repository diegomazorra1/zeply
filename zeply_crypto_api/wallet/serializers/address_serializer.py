from rest_framework import serializers

from zeply_crypto_api.wallet.models import Address


class AddressSerializer(serializers.ModelSerializer):
    cryptocurrency = serializers.CharField(source='cryptocurrency.name')
    class Meta:
        model = Address
        fields = ("id", "value", "cryptocurrency", "active", "wallet", "private_key")
