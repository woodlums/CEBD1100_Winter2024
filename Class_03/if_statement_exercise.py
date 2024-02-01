discount = 0.00
RETAIL_CUST = "R"
WHOLESALE_CUST = "W"

customer_type = input("What is the customer type? :")
invoice_amount = float(input("What is the invoice amount?"))

if customer_type.upper() == RETAIL_CUST:
    if invoice_amount >= 100.00 and invoice_amount < 250:
        discount = .1
    if invoice_amount >= 250:
        discount = .2
elif customer_type.upper() == WHOLESALE_CUST:
    if invoice_amount < 500:
        discount = .4
    if invoice_amount >= 500:
        discount = .2
else:
    print("Sorry the customer type is incorrect.")

print("The discount determined is : {:.0%}".format(discount))

