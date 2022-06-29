import random


class Account:

    def __init__(self, acc_type, balance):
        self.acc_type = acc_type
        self.balance = balance
        self.account_no = random.randint(90000000, 900000000)
        self.transactions = []

    def display_account_details(self):
        print(f"Account Type = {self.acc_type}\nAccount Number = {self.account_no}\nBalance = {self.balance}")
