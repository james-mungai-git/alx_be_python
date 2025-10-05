import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def test_addition(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.add(2, 3), 5)

    def test_subtraction(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.subtract(7, 3), 4)

    def test_multiplication(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.multiply(2, 3), 6)

    def test_division(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.divide(9, 3), 3)

    def test_division_by_zero(self):
        calc = SimpleCalculator()
        with self.assertRaises(ZeroDivisionError):
            calc.divide(5, 0)  