from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, c):
        self.colour = c

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass