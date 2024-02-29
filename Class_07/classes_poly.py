class Animal:

    def __init__(self, name):
        self.__name = name

    def make_sound(self):
        return "I'm not sure what to say!"

    def get_name(self):
        return self.__name

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"


a2 = Dog("Spot")
a3 = Cat("Felix")
a4 = Dog("Dog")
a5 = Cat("Garfield")

list_of_animals = [a2, a3, a4, a5]

for a in list_of_animals:
    print(f"My name is {a.get_name()} and the sound I make is {a.make_sound()}")


