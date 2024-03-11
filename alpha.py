from bitcoinlib.wallets import Wallet, WalletError

def display_balance(wallet):
    print("Your balance:", wallet.balance())

def send_bitcoin(wallet, recipient_address, amount):
    try:
        tx = wallet.send_to(recipient_address, amount, fee=0.0001)  # Assuming a fixed transaction fee
        print(f"Successfully sent {amount} BTC to {recipient_address}")
    except WalletError as e:
        print("Error sending bitcoin:", e)

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



# Main menu loop
while True:
    print("\n1. Display balance")
    print("2. Send bitcoin")
    print("3. Exit")

    choice = input("Please enter your choice (1/2/3): ")

    if choice == '1':
        display_balance(wallet)
    elif choice == '2':
        recipient_address = input("Enter recipient's Bitcoin address: ")
        amount = float(input("Enter amount to send: "))
        send_bitcoin(wallet, recipient_address, amount)
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
