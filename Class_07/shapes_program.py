from functools import reduce

from Shape_Entities.Circle import Circle
from Shape_Entities.Square import Square
from Shape_Entities.Rectangle import Rectangle
from Shape_Entities.Triangle import Triangle
from Shape_Entities.Shape import Shape

c1 = Circle(15, "Blue")
c2 = Circle(20, "Yellow")
s1 = Square(12, "White")
r1 = Rectangle(30, 40, "Pink")
t1 = Triangle(25, "Blue")
# x1 = Shape("Red")

print(c1)

colour_list = []
colour_list.append(c1)
colour_list.append(c2)
colour_list.append(s1)
colour_list.append(r1)
colour_list.append(t1)
# colour_list.append(x1)

area = 0

for s in colour_list:
    area = area + s.get_area()

print(f"The total area of all the shapes is {area}.")

print(reduce(lambda x, shape: x + shape.get_area(), colour_list, 0))
print(reduce(lambda x, area: x + area, map(lambda s: s.get_area(), colour_list)))
print(sum(map(lambda s: s.get_area(), colour_list)))

print("*" * 75)
for s in colour_list:
    print(round(s.get_area(), 2))
print("*" * 75)
for s in sorted(colour_list, key=lambda x: x.get_area(), reverse=True):
    print(round(s.get_area(), 2))
