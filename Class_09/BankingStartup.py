import sys
from decimal import Decimal
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, rate, initial_amount):
        self.number_deposits = 0
        self.current_balance = Decimal("0.00")
        self.total_deposits = Decimal("0.00")
        self.active = True
        self.interest_rate = rate
        self.deposit(initial_amount)


    @abstractmethod
    def deposit(self, amount: Decimal):
        self.number_deposits += 1
        self.total_deposits += amount
        self.current_balance += amount

class SavingsAccount(Account):

    def deposit(self, amount: Decimal):
        if not self.active and (self.current_balance + amount >= Decimal("25.00")):
            self.active = True
        super().deposit(amount)

    def withdraw(self, amount):
        # Check if the amount would result in < 0
        if self.current_balance - amount <= 0:
            print("You have overdrawn, account is now inactive.")
            self.active = False

    def check_overdraw(self):
        pass


s1 = SavingsAccount(Decimal(".01"), Decimal("5.00"))
s1.active = False
s1.deposit(Decimal("50.00"))

print(s1.current_balance)
print(s1.active)


print(sys.platform)


print(sys.version)