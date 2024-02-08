 # FizzBuzz

for x in range(26):
    print(str(x) + " :", end="")

    div_3 = x % 3 == 0
    div_5 = x % 5 == 0
    div_7 = x % 7 == 0


    if div_3:
        print("Fizz", end="")
    if div_5:
        print("Buzz", end="")
    if div_7:
        print("Pop", end="")

    print()
