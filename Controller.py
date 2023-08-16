from Database import Database
import datetime

class Controller:
    database = Database()

    def login(self):
        pin = input("Enter your PIN: ")
        customer = self.database.get_customer_by_pin(pin)
        while not customer:
            print("Invalid PIN. Please try again.")
            pin = input("Enter your PIN: ")
            customer = self.database.get_customer_by_pin(pin)
        return customer

    def show_balance(self,customer):
        balance = customer.get_account_balance()
        print("Account Balance: $", balance)

    def withdraw_money(self,customer):
        amount = float(input("Enter the amount to withdraw: "))
        if customer.withdraw(amount):
            self.database.update_balance(customer.account.account_number, customer.account.balance)
            self.database.add_transaction(customer.account.account_number, amount, datetime.datetime.now(), 'DR', customer.account.balance, 'Withdraw')
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    def deposit_money(self,customer):
        amount = float(input("Enter the amount to deposit: "))
        customer.deposit(amount)
        self.database.update_balance(customer.account.account_number, customer.account.balance)
        self.database.add_transaction(customer.account.account_number, amount, datetime.datetime.now(), 'CR', customer.account.balance, 'Deposit')
        print("Deposit successful.")

    def transfer_funds(self,customer):
        recipient_account_number = input("Enter the recipient's account number: ")
        amount = float(input("Enter the amount to transfer: "))
        recipient_customer = self.database.get_customer_by_account_number(recipient_account_number)
        if recipient_customer:
            if customer.transfer_funds(amount, recipient_customer.account):
                self.database.update_balance(customer.account.account_number, customer.account.balance)
                self.database.add_transaction(customer.account.account_number, amount, datetime.datetime.now(), 'DR', customer.account.balance, 'Transfer')
                print("Transfer successful.")
            else:
                print("Insufficient balance.")
        else:
            print("Recipient account not found.")

    def display_last_transactions(self,customer):
        transactions = self.database.get_last_10_transactions(customer.account.account_number)
        for transaction in transactions:
            print("Transaction ID:", transaction.transaction_id)
            print("Amount:", transaction.amount)
            print("Date:", transaction.date)
            print("Type:", transaction.transaction_type)
            print("Available Balance:", transaction.available_balance)
            print("Description:", transaction.description)
            print()

    def logout(self):
        print("Logged out.")