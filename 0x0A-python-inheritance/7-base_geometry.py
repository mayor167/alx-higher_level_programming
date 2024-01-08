#!/usr/bin/python3
"""Defines a base geometry class."""


class BaseGeometry:
    """Repr base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate parameter as integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter.
        Raises:
            TypeError: when value is not an integer.
            ValueError: when value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
