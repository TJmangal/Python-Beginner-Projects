from Account import Account
from Customer import Customer
import datetime


class BankManagement:

    def __init__(self):
        self.bank_db = {}

    def find_account(self, account_no):
        for account in self.bank_db.keys():
            if account.account_no == account_no:
                return account
        print("No such account found")
        return None

    def open_account(self, f_name, l_name, dob, address, acc_type, mobile_no):
        account_nos = [account.account_no for account in self.bank_db.keys()]
        customer_nos = [customer.cust_id for customer in self.bank_db.values()]
        account = Account(acc_type, 0)
        while account.account_no in account_nos:
            account = Account(acc_type, 0)
        customer = Customer(f_name, l_name, dob, address, mobile_no)
        while customer.cust_id in customer_nos:
            customer = Customer(f_name, l_name, dob, address, mobile_no)
        self.bank_db[account] = customer
        print(f"Account successfully opened. Your Account number = {account.account_no} & Your customer id = "
              f"{customer.cust_id}")

    def close_account(self, account_no):
        account = self.find_account(account_no)
        if account is not None:
            del self.bank_db[account]

    def view_balance(self, account_no):
        account = self.find_account(account_no)
        if account is not None:
            print(account.balance)

    def withdraw(self, amount, account_no):
        account = self.find_account(account_no)
        if account is not None:
            if account.balance >= amount:
                account.balance -= amount
                account.transactions.append(["Debit: ", amount, datetime.datetime.now()])
                print(f"Successfully debited Rs {amount}. Available balance is Rs {account.balance}")
            else:
                print("Insufficient Balance!!!")

    def deposit(self, amount, account_no):
        account = self.find_account(account_no)
        if account is not None:
            account.balance += amount
            account.transactions.append(["Credit: ", amount, datetime.datetime.now()])
            print(f"Successfully credited Rs {amount}. Available balance is Rs {account.balance}")

    def view_account_details(self, account_no):
        account = self.find_account(account_no)
        if account is not None:
            account.display_account_details()
            customer = self.bank_db[account]
            customer.display_customer_details()

    def view_customer_details(self, customer_id):
        found = False
        for customer in self.bank_db.values():
            if customer.cust_id == customer_id:
                found = True
                customer.display_customer_details()
                break
        if found:
            accounts = [account for account, customer in self.bank_db.items() if customer.cust_id == customer_id]
            if len(accounts) != 0:
                print("Accounts associated with customer are - ")
                for acc in accounts:
                    acc.display_account_details()
            else:
                print("No accounts found for this customer")
        else:
            print("No such customer found")

    def view_transaction_history(self, account_no):
        account = self.find_account(account_no)
        if account is not None:
            print("Transaction type", "Amount", "Date & Time")
            for transaction, amount, DateTime in account.transactions:
                print(transaction, amount, DateTime)
