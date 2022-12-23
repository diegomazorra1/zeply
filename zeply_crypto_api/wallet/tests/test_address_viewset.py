from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from zeply_crypto_api.wallet.models import Address, CryptoCurrency


class TestAddress(APITestCase):
    """Test address viewset"""

    def setUp(self):
        self.url = reverse('api:address-list')

    def test_create_bth_address_successful(self):
        """Testing the creation of a bitcoin address"""
        data = {
            "cryptocurrency": "btc",
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(Address.objects.all().count(), 1)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_eth_address_successful(self):
        """Testing the creation of a eth address"""
        data = {
            "cryptocurrency": "eth",
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(Address.objects.all().count(), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_address_wrong_input(self):
        """Testing the retrieve of a wrong field"""
        data = {
            "cryptocurrency": "asdaw",
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Address.objects.all().count(), 0)

    # def test_retrieve_specific_address(self):
    #     """Testing the retrieve of a specific address"""
    #     cryptocurrency = CryptoCurrency.objects.create(name='eth')
    #     address = Address.objects.create(value='fake', cryptocurrency=cryptocurrency, private_key='fake2')
    #     url = f"api/address/{address.id}"
    #     response = self.client.get(url, format='json')
    #     self.assertEqual(response.data['value'], 'fake')
    #     self.assertEqual(response.data['cryptocurrency']['name'], 'eth')
    #     self.assertEqual(response.data['private_key'], 'fake2')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
