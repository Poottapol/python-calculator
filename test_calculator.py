import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), -2)
        self.assertEqual(self.calc.subtract(2, 4), 2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(10, 5), 0)
        self.assertEqual(self.calc.modulo(10, 7), 3)

if __name__ == "__main__":
    unittest.main()
