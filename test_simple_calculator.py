import argparse
import unittest

from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def test_constructor(self):
        sc1 = SimpleCalculator(['simple_calculator.py', '-mult', '2', '2'])

        self.assertEqual(sc1.arg[0], 'simple_calculator.py')
        self.assertNotEqual(sc1.arg[0], '-mult')

        print("test_constructor - Done")

    def test_run(self):
        sc1 = SimpleCalculator(['simple_calculator.py', '-div'])

        self.assertRaises(argparse.ArgumentTypeError, sc1.run())
        print("test_run - Done")

    def test_arg_parse(self):
        self.assertTrue(SimpleCalculator.create_arg_parse())

        print("test_arg_parse - Done")

    def test_check_arg(self):
        self.assertTrue(SimpleCalculator.check_arg(['simple_calculator.py', '-mult', '2', '2']))

        self.assertFalse(SimpleCalculator.check_arg(['simple_calculator.py']))

        print("test_check_arg - Done")

    def test_addition(self):
        self.assertEqual(SimpleCalculator.addition(2, 2), 4)
        self.assertNotEqual(SimpleCalculator.addition(1, 5), 2)
        print("test_addition - Done")

    def test_subtraction(self):
        self.assertEqual(SimpleCalculator.subtraction(2, 2), 0)
        self.assertNotEqual(SimpleCalculator.subtraction(1, 5), 2)
        print("test_subtraction - Done")

    def test_multiplication(self):
        self.assertEqual(SimpleCalculator.multiplication(2, 2), 4)
        self.assertNotEqual(SimpleCalculator.multiplication(1, 5), 2)
        print("test_multiplication - Done")

    def test_division(self):
        self.assertEqual(SimpleCalculator.division(2, 2), 1)
        self.assertNotEqual(SimpleCalculator.division(1, 5), 2)
        print("test_division - Done")

        with self.assertRaises(ZeroDivisionError):
            SimpleCalculator.division(2, 0)


if __name__ == "__main__":
    unittest.main()
