# Key generator classs
import secrets
# from bitcoinlib.wallets import HDWallet, wallet_delete
# from bitcoinlib.mnemonic import Mnemonic


def hex_private_key():
    my_key = secrets.token_hex(32)
    return my_key

# passphrase = Mnemonic().generate()
# print(passphrase)
# wallet = HDWallet.create("mWallet1", keys=passphrase, network='bitcoin')
# key1 = wallet.new_key()
