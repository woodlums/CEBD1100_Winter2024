discount = 0.00
RETAIL_CUST = "R"
WHOLESALE_CUST = "W"

while True:
    customer_type = input("What is the customer type? :")
    if customer_type.upper() == RETAIL_CUST or customer_type.upper() == WHOLESALE_CUST:
        break
    print("Sorry - please enter the correct value (R or W) - try again")

invoice_amount = float(input("What is the invoice amount?")) # Accept a number



if customer_type.upper() == RETAIL_CUST:
    if invoice_amount >= 100.00 and invoice_amount < 250:
        discount = .1
    if invoice_amount >= 250:
        discount = .2
if customer_type.upper() == WHOLESALE_CUST:
    if invoice_amount < 500:
        discount = .4
    if invoice_amount >= 500:
        discount = .2


print("The discount determined is : {:.0%}".format(discount))

