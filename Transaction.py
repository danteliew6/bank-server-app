class Transaction:
    def __init__(self, transaction_id, amount, date, transaction_type, available_balance, description):
        self.__transaction_id = transaction_id
        self.__amount = amount
        self.__date = date
        self.__transaction_type = transaction_type
        self.__available_balance = available_balance
        self.__description = description