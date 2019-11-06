import argparse


class SimpleCalculator:

    def __init__(self, arg_parser=None):
        self.parser = self.arg_parse(arg_parser)

        if self.parser.sum:
            print(self.addition(self.parser.sum[0], self.parser.sum[1]))

        if self.parser.sub:
            print(self.subtraction(self.parser.sub[0], self.parser.sub[1]))

        if self.parser.mult:
            print(self.multiplication(self.parser.mult[0], self.parser.mult[1]))

        if self.parser.div:
            print(self.division(self.parser.div[0], self.parser.div[1]))

    @staticmethod
    def arg_parse(arg_parser):
        if arg_parser is None:
            print("Welcome to the simple calculator. Use '-h' argument to get the information about the commands.")

            argp = argparse.ArgumentParser()
            argp.add_argument('-sum', nargs=2, type=int, help="Add two values.")
            argp.add_argument('-sub', nargs=2, type=int, help="Subtract two values.")
            argp.add_argument('-mult', nargs=2, type=int, help="Multiply two values.")
            argp.add_argument('-div', nargs=2, type=int, help="Divise two values.")

            return argp.parse_args()
        else:
            return arg_parser

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
    SimpleCalculator()
