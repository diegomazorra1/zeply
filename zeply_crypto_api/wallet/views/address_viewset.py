from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from zeply_crypto_api.utils import key_generator
from zeply_crypto_api.utils.address_generator import AddressGenerator
from zeply_crypto_api.utils.address_validator import check_bitcoin_address
from zeply_crypto_api.wallet.models import Address
from zeply_crypto_api.wallet.models.cryptocurrency import CryptoCurrency
from zeply_crypto_api.wallet.serializers import AddressSerializer, InputAddressSerializer
from drf_spectacular.utils import extend_schema


class AddressViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,):
    """Address viewset with its methods"""
    permission_classes = (AllowAny,)
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    @extend_schema(
        request=InputAddressSerializer,
        responses={200: AddressSerializer},
    )
    def create(self, request, *args, **kwargs):
        serializer = InputAddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request_data = serializer.validated_data
        private_key = key_generator.hex_private_key()
        address_generator = AddressGenerator(private_key)
        if request_data['cryptocurrency'] == 'eth':
            value = address_generator.eth_address()
            cryptocurrency, created = CryptoCurrency.objects.get_or_create(name='eth')
        elif request_data['cryptocurrency'] == 'btc':
            value = address_generator.btc_address()
            validated = check_bitcoin_address(value)
            if not validated:
                raise ValidationError({
                    'detail': 'There is a not valid bitcoin address'
                })
            cryptocurrency, created = CryptoCurrency.objects.get_or_create(name='btc')

        address = Address.objects.create(value=value, cryptocurrency=cryptocurrency, private_key=private_key)

        return Response(AddressSerializer(address).data)
