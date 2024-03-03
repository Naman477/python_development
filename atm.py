class ATM:
    def __init__(self):
        self.accounts = [
            {"account_number": "12345678", "pin_code": "1234", "balance": 5000},
            {"account_number": "23456789", "pin_code": "5678", "balance": 3000},
        ]

    def check_account(self, account_number, pin_code):
        for account in self.accounts:
            if account["account_number"] == account_number and account["pin_code"] == pin_code:
                return account
        return None

    def check_balance(self, account):
        print(f"Your balance is: ${account['balance']}")

    def deposit(self, account, amount):
        account["balance"] += amount
        print(f"${amount} has been deposited. Your new balance is: ${account['balance']}")

    def withdraw(self, account, amount):
        if amount > account["balance"]:
            print("Insufficient funds. Please enter a smaller amount.")
        else:
            account["balance"] -= amount
            print(f"${amount} has been withdrawn. Your new balance is: ${account['balance']}")

    def start(self):
        while True:
            account_number = input("Please enter your account number: ")
            pin_code = input("Please enter your pin code: ")
            account = self.check_account(account_number, pin_code)

            if account:
                operation = input("Please enter the operation you want to perform (Check balance, Deposit, Withdraw): ")

                if operation.lower() == "check balance":
                    self.check_balance(account)
                elif operation.lower() == "deposit":
                    amount = int(input("Please enter the amount you want to deposit: "))
                    self.deposit(account, amount)
                elif operation.lower() == "withdraw":
                    amount = int(input("Please enter the amount you want to withdraw: "))
                    self.withdraw(account, amount)
                else:
                    print("Sorry, I didn't understand that. Please enter 'Check balance', 'Deposit', or 'Withdraw'.")
            else:
                print("Sorry, the account number or pin code you entered is incorrect. Please try again.")


atm = ATM()
atm.start()