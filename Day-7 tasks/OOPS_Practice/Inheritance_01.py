class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)

        self.breed = breed

    def Breed(self):
        print(f"the Breed of {self.name} is {self.breed}")

D1 = Dog("Johny","Labrador")
D1.eat()
D1.Breed()