import datetime
from decimal import Decimal


class Item:
    def __init__(self, sku: str, name: str, price: Decimal, taxable: bool):
        self.sku = sku
        self.name = name
        self.price = price
        self.taxable = taxable

    def __str__(self):
        return "{0:8s} {1:25s} ${2:.2f}".format(self.sku, self.name, self.price)


class Customer:
    def __init__(self, cust_id: int, name: str):
        self.cust_id = cust_id
        self.name = name


class Order:
    def __init__(self, customer: Customer):
        self.customer = customer
        self.item_list = []
        self.purchase_date = datetime.datetime.now()

    def add(self, item: Item):
        self.item_list.append(item)

    def remove(self, sku: str):
        for i in self.item_list:
            if i.sku == sku:
                self.item_list.remove(i)

    def get_total_price(self):
        return sum(map(lambda x: x.price, self.item_list))

    # Print order summary
    def __str__(self):
        print("SKU      NAME                    PRICE\n-----------------------------------------")
        receipt = ""
        for i in self.item_list:
            receipt = receipt + str(i) + "\n"
        return receipt


c = Customer(1, "Mary")

o1 = Order(c)
i1 = Item("12345", "Hammer", Decimal("35.00"), True)
i2 = Item("23456", "Nail", Decimal("2.00"), False)
i3 = Item("34567", "Anvil", Decimal("99.99"), True)

o1.add(i1)
o1.add(i2)
o1.add(i3)
o1.remove("23456")

print(o1.get_total_price())

print(o1)
