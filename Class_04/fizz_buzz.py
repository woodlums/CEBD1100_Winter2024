 # FizzBuzz

#rules = [(3, "Fizz"), (5, "Buzz"), (7, "Pop")]

rules = []
ans = ""

while ans.upper() != "X":
    rule = [int(input("Enter the number to match (multiple of x):")), input("What do I print for that multiple?:")]
    ans = input("Press enter for next, or enter 'X' when finished.")
    rules.append(rule)
print()
for x in range(26):
    print(str(x) + " : ", end="")
    for rule in rules:
        if x % rule[0] == 0:
            print(rule[1], end="")
    print()
