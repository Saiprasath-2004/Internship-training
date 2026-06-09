class BankAccount:
    def __init__(self):
        self.__balance = 10000

    def deposit(self,amount):
        self.__balance += amount
        print("The Deposit is Successful")
    
    def getBalance(self):
        return self.__balance
    


acc=BankAccount()

acc.deposit(400)
acc.deposit(200)
print(acc.getBalance())