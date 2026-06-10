class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")


# Creating objects
dog1 = Dog("Bruno")
cat1 = Cat("Kitty")
dog2 = Dog("Rocky")

# Polymorphism
animals = [dog1, cat1, dog2]

for animal in animals:
    animal.speak()