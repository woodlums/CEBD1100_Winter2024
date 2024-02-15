sequence2 = [1, 2, 3, 10, 20]

result = map(lambda x: x * x, sequence2)

print(list(result))

# -----------------------
# without a lambda

result2 = [x * x for x in sequence2]

print(result2)

