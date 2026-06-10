class Atm:
    def __init__(self,name,balance):
        self.name= name
        self.balance = balance

    def showbalance(self):
        print(f"The Balance of customer {self.name} is {self.balance}")

    def deposit(self,amount):
        self.balance += amount
        print("The Current Balance is",self.balance)

    def withdraw(self,amount):
        if(self.balance>amount):
            self.balance -=amount
            print("The Current Balance is",self.balance)

        else:
            print("Insufficient Balance ")


atm1=Atm('sandeep',200)
atm2=Atm('siddu',400)
atm3=Atm('jishnu',3000)

atm3.withdraw(2000)
atm2.deposit(300)
atm1.showbalance()