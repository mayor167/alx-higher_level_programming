#!/usr/bin/python3


def max_integer(my_list=[]):
    length = len(my_list)
    my_list.sort()

    if length == 0:
        biggestInt = None
    else:
        biggestInt = my_list[-1]
    return (biggestInt)
