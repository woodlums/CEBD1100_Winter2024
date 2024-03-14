from unittest import TestCase
from Square import Square
from Shape import Shape

class TestSquare(TestCase):

    def setUp(self):
        self.fcn = Square(5, "Blue")

    def test_get_area(self):
        expected = 25
        result = self.fcn.get_area()
        self.assertEqual(expected, result)

    def test_get_perimeter(self):
        expected = 20
        result = self.fcn.get_perimeter()
        self.assertEqual(expected, result)

    def test_instantiation(self):
        newfcn = Square(1, "Blue")
        self.assertIsInstance(newfcn, Shape)

