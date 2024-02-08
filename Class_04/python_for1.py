my_vals_1 = [1, 2, 3, 4, 5]
my_vals_2 = range(1, 6)

for x in my_vals_1:
    print("Two to the power of {0:} will be {1:}".format(x, 2 ** x))

converted = list(my_vals_2)
del converted[0]
for x in converted:
    print("Two to the power of {0:} will be {1:}".format(x, 2 ** x))

print(type(my_vals_1))
print(type(my_vals_2))


print(list(range(5, 20, 5)))

print(list(range(10, 15, 20)))

for a in "Brendan":
    print(a)


# For all numbers from 1 to 50,
# identify which are prime numbers.

