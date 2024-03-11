from bitcoinlib.wallets import Wallet, WalletError

# Ask for wallet name
wallet_name = input("Please enter your wallet name: ")

try:
    # Attempt to load the wallet
    wallet = Wallet(wallet_name)
    print("Wallet loaded successfully!")
except WalletError:
    print("Wallet does not exist. Creating a new wallet...")
    # Create new wallet if it doesn't exist
    wallet = Wallet.create(wallet_name)
    print("Wallet created successfully!")

# Get the private key
try:
    private_key = wallet.get_key().wif
    print("Private Key:", private_key)
except WalletError as e:
    print("Error retrieving private key:", e)
