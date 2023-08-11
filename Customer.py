class Customer:
    def __init__(self, customer_id, account, first_name, last_name, phone):
        self.customer_id = customer_id
        self.account = account
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def get_account_balance(self):
        return self.account.get_balance()

    def withdraw(self, amount):
        return self.account.withdraw(amount)

    def deposit(self, amount):
        return self.account.deposit(amount)

    def transfer_funds(self, amount, recipient_account):
        return self.account.transfer_funds(amount, recipient_account)

    def get_last_transactions(self, num_transactions):
        return self.account.get_last_transactions(num_transactions)