from rest_framework import serializers


class InputAddressSerializer(serializers.Serializer):
    cryptocurrency = serializers.ChoiceField(choices=['btc', 'eth'])
