# Review Exercise (Class 2, Ex 1)
# 1. Ask for a first number.
# 2. Ask for a second number.
# 3. Add both of them
# 4. Display the result like "The first number added to the 2nd number is : x"

print("First numbner is:", end="")
number1 = input()
print("Second number is:", end="")
number2 = input()

# number1 = int(number1)
# number2 = int(number2)
#
# total = number1 + number2

total = int(number1) + int(number2)

print("Sum of numbers " + str(total))
