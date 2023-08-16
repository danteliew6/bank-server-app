from Transaction import Transaction

class Account:
    def __init__(self, account_number, name, balance, pin):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.pin = pin
        self.transactions = []

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def deposit(self, amount):
        self.balance += amount
        return True

    def transfer_funds(self, amount, recipient_account):
        if self.withdraw(amount):
            recipient_account.deposit(amount)
            return True
        return False