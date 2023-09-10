#!/usr/bin/python3


def main():

    import sys

    sum = 0

    for count in range(len(sys.argv) - 1):
        sum += int(sys.argv[count + 1])
    print("{}".format(sum))


if __name__ == "__main__":
    main()
