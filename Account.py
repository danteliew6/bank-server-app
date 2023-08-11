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
            transaction = Transaction(len(self.transactions) + 1, -amount, 'Withdrawal',
                                      self.balance, 'Withdrawal from account')
            self.transactions.append(transaction)
            return True
        return False

    def deposit(self, amount):
        self.balance += amount
        transaction = Transaction(len(self.transactions) + 1, amount, 'Deposit',
                                  self.balance, 'Deposit into account')
        self.transactions.append(transaction)
        return True

    def transfer_funds(self, amount, recipient_account):
        if self.withdraw(amount):
            recipient_account.deposit(amount)
            transaction = Transaction(len(self.transactions) + 1, -amount, 'Transfer',
                                      self.balance, 'Transfer to account: ' + recipient_account.account_number)
            self.transactions.append(transaction)
            return True
        return False

    def get_last_transactions(self, num_transactions):
        return self.transactions[-num_transactions:]