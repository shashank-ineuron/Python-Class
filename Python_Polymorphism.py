# Function Overriding in Python

from math import pi

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        pass

    def whichShape(self):
        print(self.name)

class Square(Shape):
    def __init__(self, name, length):
        super().__init__(name)
        self.side_length = length

    def area(self):
        print(self.side_length**2)

    def fact(self):
        print("Square has each angle equalt to 90 degrees")

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.circle_radius = radius

    def area(self):
        print(pi * (self.circle_radius**2))

sq = Square("Square", 4)
cr = Circle("Circle", 5)
sq.area()
cr.area()
sq.fact()
cr.fact()

sq.whichShape()
cr.whichShape()
