from Customer import Customer
from Account import Account

class Database:
    accounts = {
        '1': Customer('1', Account('123876', 'Savings', 0, '123456'), 'dante', 'liew', '12345678'),
        '2': Customer('2', Account('456109', 'Checking', 1000, '654321'), 'helena', 'chen', '87654321'),
        '3': Customer('3', Account('789686', 'Savings', 500, '987654'), 'jane', 'smith', '1357924'),
        '4': Customer('4', Account('101112', 'Checking', 2000, '111000'), 'alex', 'brown', '2468135'),
        '5': Customer('5', Account('131415', 'Savings', 100, '514235'), 'sarah', 'lee', '9753186'),
        '6': Customer('6', Account('161718', 'Checking', 750, '817263'), 'michael', 'wilson', '6248719'),
        '7': Customer('7', Account('192021', 'Savings', 2500, '202192'), 'emily', 'roberts', '3197246'),
        '8': Customer('8', Account('222324', 'Checking', 1500, '423524'), 'jason', 'nguyen', '6275319'),
        '9': Customer('9', Account('252627', 'Savings', 300, '726525'), 'lisa', 'smith', '9524137'),
        '10': Customer('10', Account('282930', 'Checking', 5000, '303828'), 'kevin', 'brown', '7162539'),
        '11': Customer('11', Account('313233', 'Savings', 200, '333131'), 'natalie', 'wilson', '4297516'),
        '12': Customer('12', Account('343536', 'Checking', 1000, '635434'), 'ryan', 'jackson', '8172635'),
        '13': Customer('13', Account('373839', 'Savings', 1500, '938737'), 'laura', 'thompson', '5241638'),
        '14': Customer('14', Account('373839', 'Savings', 1500, '938737'), 'laura', 'thompson', '5241638'),
        '15': Customer('15', Account('404142', 'Checking', 2500, '241404'), 'stephen', 'martinez', '8379251'),
        '16': Customer('16', Account('434445', 'Savings', 500, '544343'), 'olivia', 'harris', '1625349'),
        '17': Customer('17', Account('464748', 'Checking', 10000, '847464'), 'matthew', 'rodriguez', '9531472'),
        '18': Customer('18', Account('495051', 'Savings', 1000, '150594'), 'amanda', 'thomas', '4268153'),
        '19': Customer('19', Account('525354', 'Checking', 750, '453252'), 'nicole', 'white', '7391526'),
        '20': Customer('20', Account('555657', 'Savings', 2000, '755558'), 'adam', 'clark', '2619375')
    }

    def add_customer(self, customer):
        self.accounts[customer.customer_id] = customer

    def get_customer_by_pin(self, pin):
        for customer in self.accounts.values():
            if customer.account.pin == pin:
                return customer
        return None

    def get_customer_by_account_number(self, account_number):
        for customer in self.accounts.values():
            if customer.account.account_number == account_number:
                return customer
        return None