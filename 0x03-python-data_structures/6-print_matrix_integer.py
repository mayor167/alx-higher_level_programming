#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for line in matrix:
            for item in line:
                if line.index(item) != len(line) - 1:
                    endspace = " "
                else:
                    endspace = ""
                print("{:d}".format(item), end=endspace)
            print()
