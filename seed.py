from bitcoinlib.wallets import Wallet, wallet_delete
from bitcoinlib.mnemonic import Mnemonic

passphrase = Mnemonic().generate()
print(passphrase)
w = Wallet.create("Wallet99", keys=passphrase, network='bitcoin')

w.get_key()
w.info()

# sister polar bulk drill summer sauce thought quantum afraid flock armed excite