from Class_07.Shape_Entities.Shape import Shape

class Triangle(Shape):

    def __init__(self, l, c):
        self.length = l
        super().__init__(c)

    def get_perimeter(self):
        return self.length * 4

    def get_area(self):
        return 0