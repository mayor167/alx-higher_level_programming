#!/usr/bin/python3

def main():
    import sys
    i = 0
    length = len(sys.argv)

    if length == 1:
        print("{} arguments.".format(i))
    i = 1
    if length == 2:
        print("{} argument:".format(i))
        print("{}: {}".format(i, sys.argv[i]))

    if length > 2:
        print("{} arguments:".format(length - 1))
        for i in range(length):
            if i != 0:
                print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
