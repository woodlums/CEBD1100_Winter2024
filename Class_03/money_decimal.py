from decimal import Decimal

a = Decimal(55.44)

b = Decimal(55.54)

c = Decimal("55.44")

d = Decimal(8)

b = b - Decimal(.10)

print(type(a))

print(a)

print(a == b)

print(type(c))
print(c)

c = c * 2

print(c)
print(d)