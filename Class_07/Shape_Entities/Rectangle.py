from Class_07.Shape_Entities.Square import Square

class Rectangle(Square):

    def __init__(self, l, h, c):
        self.height = h
        super().__init__(l, c)

    def get_area(self):
        return self.length * self.height

    def get_perimeter(self):
        return (self.length * 2) + (self.height * 2)
