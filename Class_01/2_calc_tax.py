# Example of how to use constants instead of hard-coding numbers.

TAX_RATE = 1.14975
price = 59.99

grand_total = price * TAX_RATE

# To convert to string, use function --->  str(....)
# to convert to a float, use function ---> float(....)

print("The price with tax is " + str(grand_total))
