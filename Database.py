from Customer import Customer
from Account import Account

class Database:
    accounts = {
        '1': Customer('1', Account('123', [], 'Savings', 0, '123456'), 'dante', 'liew', '12345678')
    }