#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    result = [[1]]

    for num in range(1, n):
        new_row = [1]
        for line in range(1, num):
            new_item = result[num - 1][line - 1] + result[num - 1][line]
            new_row.append(new_item)

        new_row.append(1)
        result.append(new_row)

    return result

