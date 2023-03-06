import random


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import registry
from sqlalchemy import create_engine


# Create engine
'''
Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
Scheme: engine = create_engine("sqlite:////absolute/path/to/foo.db")
'''
URI = "sqlite:////Users/wojciechflak/PycharmProjects/Python-tutorials/db_for_sqlalchemy_tutorial.db"
engine = create_engine(URI)


# Create table in db
Base = registry().generate_base()

class BankAccounts(Base):

    __tablename__ = 'bank_accounts'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    balance = Column(Integer)
    account_number = Column(Integer)


    def __init__(self, id, name, balance, account_number):
        self.id = id
        self.name = name
        self.balance = balance
        self.account_number = account_number


    @classmethod
    def account_number(cls):
        digit_list = []
        for digit in range(10):
            rand_digit = random.randint(1, 9)
            digit_list.append(rand_digit)
        acc_number = ''.join(map(str, digit_list))
        return acc_number


if __name__ == '__main__':
    # Create table from class
    Base.metadata.create_all(engine)

    print(BankAccounts.account_number())


acc1 = BankAccounts(name='Agata', account_number=BankAccounts.account_number, balance=1000)





# class BankAccount:
#
#     def __init__(self, name, balance=00):
#
#         self.name = name
#         self.balance = balance
#         self.account_number = BankAccount.account_number()
#         cursor.execute('''CREATE TABLE IF NOT EXISTS bank_accounts
#                             (id INTEGER PRIMARY KEY, name TEXT, account_number INTEGER, balance INTEGER)''')
#         adding_to_db = '''INSERT INTO bank_accounts (name, account_number, balance)
#                         VALUES (?, ?, ?)'''
#         cursor.execute(adding_to_db, (self.name, self.account_number, self.balance))
#         connection.commit()
#
#     @staticmethod
#     def account_number():
#         digit_list = []
#         for digit in range(10):
#             rand_digit = random.randint(1, 9)
#             digit_list.append(rand_digit)
#         acc_number = ''.join(map(str, digit_list))
#         return acc_number
#
#     @staticmethod
#     def get_balance(account_number):
#         g_b = '''SELECT balance FROM bank_accounts WHERE account_number = {}'''.format(account_number)
#         balance = cursor.execute(g_b).fetchone()[0]
#         return balance
#
#     @classmethod
#     def deposit(cls, account_number, amount):
#         balance = cls.get_balance(account_number)
#         depo = '''UPDATE bank_accounts SET balance = {} WHERE account_number = {}'''.format(balance + amount,
#                                                                                             account_number)
#         cursor.execute(depo)
#         connection.commit()
#         return
#
#     @classmethod
#     def withdrawal(cls, account_number, amount):
#         balance = cls.get_balance(account_number)
#         if balance >= amount:
#             depo = '''UPDATE bank_accounts SET balance = {} WHERE account_number = {}'''.format(balance - amount,
#                                                                                                 account_number)
#             cursor.execute(depo)
#             connection.commit()
#         else:
#             print('Balance is too low.')
#         return
#
#     @classmethod
#     def delete_account(cls, name, account_number, permission=False):
#         if name and account_number and permission:
#             del_acc = '''DELETE FROM bank_accounts WHERE account_number = {}'''.format(account_number)
#             cursor.execute(del_acc)
#             connection.commit()
#         else:
#             print('Unable to delete account')
#
#
# connection = sqlite3.connect('bank-accounts.db',)
# cursor = connection.cursor()
# connection.set
# with cursor as cursor:
#     cursor.execute
# # BankAccount.delete_account('pawel', 5825222938,permission=True)
# # print(BankAccount.get_balance(4252595441))
# # wlodek = BankAccount('Wlodek', 2340)
# # BankAccount.deposit(account_number=4252595441, amount=1233)
# # BankAccount.withdrawal(4252595441, 2000)
