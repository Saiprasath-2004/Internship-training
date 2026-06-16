from abc import ABC , abstractmethod
from datetime import datetime

class User:
    def __init__(self, name,balance):
        self.name = name
        self.__balance = balance
        self.wallet = Wallet()
    
    def show_balance(self):
        return self.__balance
    
    def deduct_balance(self,amount):
        self.__balance -= amount 

    def add_balance(self,amount):
        self.__balance += amount

    def display_balance(self):
        print(f"Current Balance: {self.show_balance()}")

class payment(ABC):

    @abstractmethod
    def make_payment(self,user,amount):
        pass

    def process_payment(self,user,amount):
        if amount <= user.show_balance():
            user.deduct_balance(amount)
            return True
        return False

class UPI(payment):
    def __init__(self,upi_id):
        self.upi_id=upi_id
    
    def make_payment(self,user,amount):
        if self.process_payment(user,amount):
            transaction = Transaction(
                user.name,
                None,
                amount,
                "UPI",
                "Success"
            )

            user.wallet.add_transaction(transaction)
            print("UPI Payment is Successful ")
        else:
            print("Insufficient Balance")

    def transfer_money(self,sender,receiver,amount):
        if amount <= sender.show_balance():
            sender.deduct_balance(amount)
            receiver.add_balance(amount)
            transaction = Transaction(
                sender.name,
                receiver.name,
                amount,
                "UPI",
                "Success"
            )
            sender.wallet.add_transaction(
                transaction
            )
            receiver.wallet.add_transaction(transaction)
            print("Transfer Successful")
        else:
            print("Insufficient Balance ")
        

class CreditCard(payment):
    def __init__(self,cardno):
        self.cardno=cardno

    def make_payment(self, user, amount):
        
        if self.process_payment(user,amount):
            transaction = Transaction(
                user.name,
                None,
                amount,
                "Credit Card",
                "Success"
            )

            user.wallet.add_transaction(transaction)
            print("Credit Card Payment Successful ")
        else:
            print("Insufficient Balance")



class Transaction:
    transaction_counter = 1
    def __init__(self,sender,receiver,amount,payment_method,status):
        self.transaction_id= (
            f"TXN{Transaction.transaction_counter}"
        )
        Transaction.transaction_counter +=1
        self.sender=sender
        self.receiver=receiver
        self.amount=amount
        self.payment_method = payment_method
        self.status=status

        self.timestamp = datetime.now()
        
    def __str__(self):
        return(
            f"Transaction ID: {self.transaction_id}\n"
            f"Sender: {self.sender}\n"
            f"Receiver: {self.receiver}\n"
            f"Amount: {self.amount}\n"
            f"Payment Method: {self.payment_method}\n"
            f"status: {self.status}\n" 
            f"status: {self.timestamp}\n"
        )
    
class Wallet:
    def __init__(self):
        self.transactions = []
    
    def add_transaction(self,transaction):
        self.transactions.append(transaction)

    def show_transactions(self):

        if not self.transactions:
            print("No transactions found")
            return
        
        for transaction in self.transactions:
            print(transaction)
            print("-"*20)


# Users

user1 = User("Sai", 50000)
user2 = User("Rahul", 10000)

# Payment Methods

upi = UPI("sai@ybl")
card = CreditCard("123456")

# Initial Balances

print("\nInitial Balances")
print(f"{user1.name}:")
user1.display_balance()

print(f"{user2.name}:")
user2.display_balance()

# UPI Payment

print("\nUPI Payment")
upi.make_payment(user1, 1000)

# Credit Card Payment

print("\nCredit Card Payment")
card.make_payment(user1, 2000)

# Transfer Money

print("\nMoney Transfer")
upi.transfer_money(
    user1,
    user2,
    5000
)

# Final Balances

print("\nFinal Balances")

print(f"{user1.name}:")
user1.display_balance()

print(f"{user2.name}:")
user2.display_balance()

# Transaction History

print(f"\n{user1.name} Wallet Transactions")
user1.wallet.show_transactions()

print(f"\n{user2.name} Wallet Transactions")
user2.wallet.show_transactions()