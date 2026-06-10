class payment:
    def pay(self):
        pass


class Upi(payment):
    def pay(self):
        print("the Upi payment was successful")
    
class Card(payment):
    def pay(self):
       print("the card payment was successful") 

class Wallet(payment):
    def pay(self):
        print("the Wallet payment was successful")

payments = [
    Upi(),
    Card(),
    Wallet()
]

for p in payments:
    p.pay()