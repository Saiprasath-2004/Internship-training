import math


class Shape:
    def __init__(self, shape_name):
        self.shape_name = shape_name

    def area(self):
        pass

    def __str__(self):
        return f"Shape: {self.shape_name}"


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius



rectangle = Rectangle(10, 5)
circle = Circle(7)

print(rectangle)
print("Rectangle Area =", rectangle.area())

print(circle)
print("Circle Area =", round(circle.area(), 2))