#!/usr/bin/python3


def main():
    from calculator_1 import add, sub, mul, div

    import sys

    length = len(sys.argv) - 1

    if length != 3:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    lOp = {"+": add, "-": sub, "*": mul, "/": div}

    if sys.argv[2] not in list(lOp.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, lOp[sys.argv[2]](a, b)))


if __name__ == "__main__":
    main()
