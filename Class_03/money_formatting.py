my_amount = 8.88
my_other_amount = 9.99

# Fixed money format.
# i18n
print("The value is: ${0:.2f} or this amount ${0:.2f}.".format(my_amount, my_other_amount))

print("The value is: ${val:.2f} or this amount ${val:.2f}.".format(
    val=my_amount,
    my_other_amount=my_other_amount))

print("The percentage of the tax is {:.2%}".format(.55))

print(f"The percentage of the tax is also {.55}")

print(str(my_amount) + " " + str(my_other_amount))

print(f"{my_amount} {my_other_amount}")


