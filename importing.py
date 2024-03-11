from bitcoinlib.wallets import Wallet

# Use a masterkey WIF when creating a wallet
wif = 'xprv9yVKhAYTdRKiFaAoSP7kLcqGSQRC4v6NU6E9NWQaiY1QYqnYAMuop9cUHnimDwy1GrXwbTkXzd3nPosL3jUn5RTWkUqYJdJLcGzZ9vymsPf'
      
# Attempt to create the wallet


try:
    w = Wallet.create('jam', wif)
    print("Wallet 'jam' created successfully.")
except Exception as e:
    print("Error creating wallet:", e)
