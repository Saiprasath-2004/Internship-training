from abc import ABC,abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self,amount):
        pass


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} via UPI")


class Card(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} via Card")


class Wallet(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} via Wallet")


payments = [
    UPI(),
    Card(),
    Wallet()
]

for p in payments:
    p.pay(1000)