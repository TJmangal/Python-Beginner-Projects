import random


class Customer:

    def __init__(self, f_name, l_name, dob, address, mobile_no):
        self.f_name = f_name
        self.l_name = l_name
        self.dob = dob
        self.address = address
        self.mobile_no = mobile_no
        self.cust_id = random.randint(10000000, 9000000000)

    def display_customer_details(self):
        print(f"First Name = {self.f_name}\nLast Name = {self.l_name}\nDate of Birth = {self.dob}\n"
              f"Address = {self.address}\nCustomer ID = {self.cust_id}\nMobile No = {self.mobile_no}")
