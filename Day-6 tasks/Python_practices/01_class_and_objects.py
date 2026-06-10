class Car:
    def __init__(self,brand,model,speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def drive(self):
        print(f"{self.brand} {self.model} is driving at {self.speed}km/hr ")


car1 = Car('BMW','X5',150)
car2 = Car('Audi','X9',110)
car3 = Car('Ferrari','V7',220)

car1.drive()
car2.drive()
car3.drive()
