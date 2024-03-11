from bitcoinlib.wallets import Wallet

# Create a wallet on the Bitcoin mainnet
wallet_name = input('Enter wallet name ')
wallet = Wallet(wallet_name)

# Get the first key (address) from the wallet
key1 = wallet.get_key()
wallet.scan()
wallet.info()

# Print the address associated with the first key
print("Wallet Address:", key1.address)
# 1E74cxywKnT3rxXXEAcMsViCEZ45bNYyuU