from Shape_Entities.Circle import Circle
from Shape_Entities.Square import Square
from Shape_Entities.Rectangle import Rectangle

c1 = Circle(15, "Blue")
c2  = Circle(20, "Yellow")
s1 = Square(12, "White")
r1 = Rectangle(30, 40, "Pink")

colour_list = []
colour_list.append(c1)
colour_list.append(c2)
colour_list.append(s1)
colour_list.append(r1)

area = 0

for s in colour_list:
    area = area + s.get_area()

print(f"The total area of all the shapes is {area}.")
