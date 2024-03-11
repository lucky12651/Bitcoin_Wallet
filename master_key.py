from bitcoinlib.wallets import Wallet

# Create a wallet on the Bitcoin mainnet
wallet_name = input('Enter wallet name ')
wallet = Wallet(wallet_name)

# Obtain the WIF encoded public master key
private_master_key_wif = wallet.account(0).key().wif_private()

# Print the public master key
print("Private Master Key (WIF):", private_master_key_wif)

