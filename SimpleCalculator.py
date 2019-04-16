import argparse


class SimpleCalculator:

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
    argp = argparse.ArgumentParser()
    print("Welcome to the simple calculator. Use '-h' argument to get information about the commands.")
    argp.add_argument('-sum', nargs=2, type=int, help="Add two values.")
    argp.add_argument('-sub', nargs=2, type=int, help="Subtract two values.")
    argp.add_argument('-mult', nargs=2, type=int, help="Multiply two values.")
    argp.add_argument('-div', nargs=2, type=int, help="Divise two values.")

    parser = argp.parse_args()

    sc = SimpleCalculator()

    if parser.sum:
        print(sc.addition(parser.sum[0], parser.sum[1]))

    if parser.sub:
        print(sc.subtraction(parser.sub[0], parser.sub[1]))

    if parser.mult:
        print(sc.multiplication(parser.mult[0], parser.mult[1]))

    if parser.div:
        print(sc.division(parser.div[0], parser.div[1]))