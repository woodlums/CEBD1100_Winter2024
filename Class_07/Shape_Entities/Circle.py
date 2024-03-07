from Class_07.Shape_Entities.Shape import Shape
from math import pi

class Circle(Shape):
    def __init__(self, r, c):
        self.radius = r
        super().__init__(c)
        #self.colour = c

    def __str__(self):
        return (f"I am a {type(self)}, my colour is {self.colour},"
                f" my area is {self.get_area()} and my perimeter is {self.get_perimeter()}")

    def get_area(self):
        return (pi * self.radius) ** 2

    def get_perimeter(self):
        return 2 * pi * self.radius
