# Address creator classs

import secrets
from bit import Key
from eth_account import Account


class AddressGenerator(object):
    """
    Generator Address class
    """

    def __init__(self, private_key):
        self.private_key = private_key

    def eth_address(self):
        private_key = self.private_key
        acct = Account.from_key(private_key)
        address = "0x" + acct.address
        return address

    def btc_address(self):
        key = Key.from_hex(self.private_key)
        address = key.address
        return address
