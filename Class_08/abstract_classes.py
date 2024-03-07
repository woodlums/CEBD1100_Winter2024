from abc import ABC, abstractmethod

# Step 1:  Import ABC+abstractmethod
# Step 2:  From your base class, inherit from ABC
# Step 3:  Anotate your functions with @abstractmethod whenever needed.

class Polygon(ABC):

    @abstractmethod
    def state_sides(self):
        pass

    @abstractmethod
    def say_hello(self):
        print("Hello")

class Triangle(Polygon):

    # overriding abstract method
    def state_sides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def state_sides(self):
        print("I have 5 sides")


shape1 = Triangle()
