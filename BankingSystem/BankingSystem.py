from Features import BankManagement


if __name__ == '__main__':
    My_Bank = BankManagement()
    print()
    print("WELCOME TO MY BANK".center(50, "*"))
    print("We strive to make your experience better".center(50))
    print()
    print("MAIN MENU".center(50, "-"))
    print("Select 1 to open an account")
    print("Select 2 to close an account")
    print("Select 3 to view balance")
    print("Select 4 to withdraw from your account")
    print("Select 5 to deposit in your account")
    print("Select 6 to view customer details")
    print("Select 7 to view account details")
    print("Select 8 to view transaction history")
    print("Select 9 to exit")

    while True:
        user_selection = input("\nEnter your selection: ").strip()
        if user_selection == "1":
            My_Bank.open_account(input("Enter first name: "), input("Enter last name: "),
                                 input("Enter date of birth: "), input("Enter address: "),
                                 input("Which account do you want to open? "), input("Enter your mobile number: "))

        elif user_selection == "2":
            My_Bank.close_account(int(input("Enter the account number that you want to close: ")))
        elif user_selection == "3":
            My_Bank.view_balance(int(input("Enter the account number: ")))
        elif user_selection == "4":
            My_Bank.withdraw(int(input("Enter the amount you want to withdraw: ")),
                             int(input("Enter your account number: ")))
        elif user_selection == "5":
            My_Bank.deposit(int(input("Enter the amount you want to deposit: ")),
                            int(input("Enter your account number: ")))
        elif user_selection == "6":
            My_Bank.view_customer_details(int(input("Enter the customer id: ")))
        elif user_selection == "7":
            My_Bank.view_account_details(int(input("Enter your account number: ")))
        elif user_selection == "8":
            My_Bank.view_transaction_history(int(input("Enter your account number: ")))
        elif user_selection == "9":
            print("Thank you for banking with us. Have a nice day!")
            break
        else:
            print("Invalid Input!!!")
