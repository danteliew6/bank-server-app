from Database import Database

def login():
    pin = input("Enter your PIN: ")
    customer = database.get_customer_by_pin(pin)
    while not customer:
        print("Invalid PIN. Please try again.")
        pin = input("Enter your PIN: ")
        customer = database.get_customer_by_pin(pin)
    return customer

def show_balance(customer):
    balance = customer.get_account_balance()
    print("Account Balance: $", balance)

def withdraw_money(customer):
    amount = float(input("Enter the amount to withdraw: "))
    if customer.withdraw(amount):
        print("Withdrawal successful.")
    else:
        print("Insufficient balance.")

def deposit_money(customer):
    amount = float(input("Enter the amount to deposit: "))
    customer.deposit(amount)
    print("Deposit successful.")

def transfer_funds(customer):
    recipient_account_number = input("Enter the recipient's account number: ")
    amount = float(input("Enter the amount to transfer: "))
    recipient_customer = database.get_customer_by_account_number(recipient_account_number)
    if recipient_customer:
        if customer.transfer_funds(amount, recipient_customer.account):
            print("Transfer successful.")
        else:
            print("Insufficient balance.")
    else:
        print("Recipient account not found.")

def display_last_transactions(customer):
    num_transactions = 10
    transactions = customer.get_last_transactions(num_transactions)
    for transaction in transactions:
        print("Transaction ID:", transaction.transaction_id)
        print("Amount:", transaction.amount)
        print("Date:", transaction.date)
        print("Type:", transaction.transaction_type)
        print("Available Balance:", transaction.available_balance)
        print("Description:", transaction.description)
        print()

def logout():
    print("Logged out.")

database = Database()
customer = login()
if customer:
    options = {
        1: show_balance,
        2: withdraw_money,
        3: deposit_money,
        4: transfer_funds,
        5: display_last_transactions,
        6: logout
    }

    while True:
        print("\nActions:")
        print("1. Show Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Transfer Funds")
        print("5. Display Last 10 Transactions")
        print("6. Log out")

        choice = int(input("Enter your choice (1-6): "))

        if choice in options:
            options[choice](customer)
        else:
            print("Invalid choice. Please try again.")

        if choice == 6:
            break
else:
    print("Login failed.")