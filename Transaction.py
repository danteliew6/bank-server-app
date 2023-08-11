import datetime
class Transaction:
    def __init__(self, transaction_id, amount, transaction_type, available_balance, description):
        self.transaction_id = transaction_id
        self.amount = amount
        self.date = datetime.datetime.now()
        self.transaction_type = transaction_type
        self.available_balance = available_balance
        self.description = description