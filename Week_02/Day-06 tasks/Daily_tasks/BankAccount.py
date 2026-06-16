class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def show_balance(self):
        print(f"The balance of {self.account_holder} is {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful. Current balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal successful. Current balance: {self.balance}")
        else:
            print("Insufficient balance")


account1 = BankAccount("Sandeep", 200)
account2 = BankAccount("Siddu", 400)
account3 = BankAccount("Jishnu", 3000)

account3.withdraw(2000)
account2.deposit(300)
account1.show_balance()