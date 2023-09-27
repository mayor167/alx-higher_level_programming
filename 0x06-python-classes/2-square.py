#!/usr/bin/python3


class Square:
    pass

    def __init__(self, size):
        pass

        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
