from Customer import Customer
from Account import Account
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

class Database:
    connection = create_connection("localhost", "root", "danteliew6", "bank_server")

    # def __init__(self) -> None:
    #     self.accounts = {
    #         '1': Customer('1', Account('123876', 'Savings', 500, '123456'), 'dante', 'liew', '12345678'),
    #         '2': Customer('2', Account('456109', 'Savings', 1000, '654321'), 'helena', 'chen', '87654321'),
    #         '3': Customer('3', Account('789686', 'Savings', 500, '987654'), 'jane', 'smith', '1357924'),
    #         '4': Customer('4', Account('101112', 'Savings', 2000, '111000'), 'alex', 'brown', '2468135'),
    #         '5': Customer('5', Account('131415', 'Savings', 100, '514235'), 'sarah', 'lee', '9753186'),
    #         '6': Customer('6', Account('161718', 'Savings', 750, '817263'), 'michael', 'wilson', '6248719'),
    #         '7': Customer('7', Account('192021', 'Savings', 2500, '202192'), 'emily', 'roberts', '3197246'),
    #         '8': Customer('8', Account('222324', 'Savings', 1500, '423524'), 'jason', 'nguyen', '6275319'),
    #         '9': Customer('9', Account('252627', 'Savings', 300, '726525'), 'lisa', 'smith', '9524137'),
    #         '10': Customer('10', Account('282930', 'Savings', 5000, '303828'), 'kevin', 'brown', '7162539'),
    #         '11': Customer('11', Account('313233', 'Savings', 200, '333131'), 'natalie', 'wilson', '4297516'),
    #         '12': Customer('12', Account('343536', 'Savings', 1000, '635434'), 'ryan', 'jackson', '8172635'),
    #         '13': Customer('13', Account('373839', 'Savings', 1500, '938737'), 'laura', 'thompson', '5241638'),
    #         '14': Customer('14', Account('373839', 'Savings', 1500, '938737'), 'laura', 'thompson', '5241638'),
    #         '15': Customer('15', Account('404142', 'Savings', 2500, '241404'), 'stephen', 'martinez', '8379251'),
    #         '16': Customer('16', Account('434445', 'Savings', 500, '544343'), 'olivia', 'harris', '1625349'),
    #         '17': Customer('17', Account('464748', 'Savings', 10000, '847464'), 'matthew', 'rodriguez', '9531472'),
    #         '18': Customer('18', Account('495051', 'Savings', 1000, '150594'), 'amanda', 'thomas', '4268153'),
    #         '19': Customer('19', Account('525354', 'Savings', 750, '453252'), 'nicole', 'white', '7391526'),
    #         '20': Customer('20', Account('555657', 'Savings', 2000, '755558'), 'adam', 'clark', '2619375')
    #     }

    def add_customer(self, customer):
        sql = "INSERT INTO CUSTOMER (first_name, last_name, phone) values (%s, %s, %s)"
        val = [(customer.first_name, customer.last_name, customer.phone)]
        cursor = self.connection.cursor()
        cursor.executemany(sql,val)
        self.connection.commit()

    def get_customer_by_pin(self, pin):
        query = f"SELECT * FROM CUSTOMER left join ACCOUNT on customer.customer_id = account.account_id where account.pin = {pin}"
        result = execute_read_query(self.connection,query)
        customer_tuple = result[0]
        customer = Customer(customer_tuple[0], Account(customer_tuple[6], customer_tuple[7], customer_tuple[8], customer_tuple[9]), customer_tuple[1], customer_tuple[2], customer_tuple[3])
        return customer


    def get_customer_by_account_number(self, account_number):
        query = f"SELECT * FROM CUSTOMER WHERE left join ACCOUNT on customer.customer_id = account.account_id where account.account_id = {account_number}"
        result = execute_read_query(self.connection,query)
        customer_tuple = result[0]
        customer = Customer(customer_tuple[0], Account(customer_tuple[6], customer_tuple[7], customer_tuple[8]), customer_tuple[1], customer_tuple[2], customer_tuple[3])
        return customer