#!/usr/bin/python3
"""Defines a square print function."""


def print_square(size):
    """Print square with the # character.

    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for item in range(size):
        [print("#", end="") for num in range(size)]
        print("")