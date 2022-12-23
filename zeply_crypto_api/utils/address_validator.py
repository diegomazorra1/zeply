# Address validator module
from hashlib import sha256

digits58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'


def _decode_base58(address, length):
    n = 0
    for char in address:
        n = n * 58 + digits58.index(char)
    return n.to_bytes(length, 'big')


def check_bitcoin_address(address):
    try:
        bcbytes = _decode_base58(address, 25)
        return bcbytes[-4:] == sha256(sha256(bcbytes[:-4]).digest()).digest()[:4]
    except Exception:
        return False
