 # FizzBuzz

rules = [(3, "Fizz"), (5, "Buzz"), (7, "Pop")]

for x in range(26):
    print(str(x) + " : ", end="")
    for rule in rules:
        if x % rule[0] == 0:
            print(rule[1], end="")
    print()
