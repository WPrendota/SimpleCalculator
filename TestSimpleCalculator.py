import unittest

from types import SimpleNamespace
from SimpleCalculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.sc = SimpleCalculator(SimpleNamespace(div=None, mult=None, sub=None, sum=None))

    def test_arg_parse(self):
        self.assertEqual(SimpleCalculator.arg_parse(self, SimpleNamespace(div=[2, 2], mult=None, sub=None, sum=None)),
                         SimpleNamespace(div=[2, 2], mult=None, sub=None, sum=None))
        self.assertEqual(SimpleCalculator.arg_parse(self, SimpleNamespace(div=None, mult=[2, 2], sub=None, sum=None)),
                         SimpleNamespace(div=None, mult=[2, 2], sub=None, sum=None))
        self.assertEqual(SimpleCalculator.arg_parse(self, SimpleNamespace(div=None, mult=None, sub=[2, 2], sum=None)),
                         SimpleNamespace(div=None, mult=None, sub=[2, 2], sum=None))
        self.assertEqual(SimpleCalculator.arg_parse(self, SimpleNamespace(div=None, mult=None, sub=None, sum=[2, 2])),
                         SimpleNamespace(div=None, mult=None, sub=None, sum=[2, 2]))

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