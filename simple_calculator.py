import argparse
import logging
import sys


class SimpleCalculator:

    def __init__(self, arg=None):
        self.arg = arg
        self.argp = self.create_arg_parse()

    def run(self):
        self.check_arg(self.arg)

        try:
            if self.argp.parse_args().sum:
                print(self.addition(self.argp.parse_args().sum[0], self.argp.parse_args().sum[1]))

            if self.argp.parse_args().sub:
                print(self.subtraction(self.argp.parse_args().sub[0], self.argp.parse_args().sub[1]))

            if self.argp.parse_args().mult:
                print(self.multiplication(self.argp.parse_args().mult[0], self.argp.parse_args().mult[1]))

            if self.argp.parse_args().div:
                print(self.division(self.argp.parse_args().div[0], self.argp.parse_args().div[1]))
        except Exception:
            logging.error('Failed.', exc_info=True)

    @staticmethod
    def create_arg_parse():
        argp = argparse.ArgumentParser()
        argp.add_argument('-sum', nargs=2, type=int, help="Add two values.")
        argp.add_argument('-sub', nargs=2, type=int, help="Subtract two values.")
        argp.add_argument('-mult', nargs=2, type=int, help="Multiply two values.")
        argp.add_argument('-div', nargs=2, type=int, help="Divise two values.")

        return argp

    @staticmethod
    def check_arg(arg):
        if len(arg) > 1:
            print("Welcome to the simple calculator. Use '-h' argument to get the information about the commands.")
            return True
        else:
            print("Please give an arguments. Use '-h' to list them.")
            return False

    @staticmethod
    def addition(val_1, val_2):
        return val_1 + val_2

    @staticmethod
    def subtraction(val_1, val_2):
        return val_1 - val_2

    @staticmethod
    def multiplication(val_1, val_2):
        return val_1 * val_2

    @staticmethod
    def division(val_1, val_2):
        return val_1 / val_2


if __name__ == "__main__":
    sc = SimpleCalculator(sys.argv)
    sc.run()
