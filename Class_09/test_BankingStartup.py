from unittest import TestCase
from BankingStartup import *
from decimal import Decimal

class TestSavingsAccount(TestCase):

    def setUp(self):
        self.s1 = SavingsAccount(Decimal("0.01"), Decimal("5.00"))

    def test_new_account(self):
        expected_balance = Decimal("5.00")
        savings = SavingsAccount(Decimal("0.01"), Decimal("5.00"))
        self.assertEqual(expected_balance, savings.current_balance)

    def test_deposit(self):
        # Assemble
        expected = Decimal("15.00")
        deposit_amount = Decimal("10.00")

        # Act
        self.s1.deposit(deposit_amount)
        result = self.s1.current_balance

        # Assert
        self.assertEqual(result, expected)

    def tearDown(self):
        del self.s1
