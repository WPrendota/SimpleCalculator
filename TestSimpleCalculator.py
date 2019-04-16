import unittest
from SimpleCalculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(SimpleCalculator.addition(2, 2), 4)

    def test_subtraction(self):
        self.assertEqual(SimpleCalculator.subtraction(2, 2), 0)

    def test_multiplication(self):
        self.assertEqual(SimpleCalculator.multiplication(2, 2), 4)

    def test_division(self):
        self.assertEqual(SimpleCalculator.division(2, 2), 1)

        with self.assertRaises(ZeroDivisionError):
            SimpleCalculator.division(2, 0)


if __name__ == "__main__":
    unittest.main()