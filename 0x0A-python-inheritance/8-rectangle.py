#!/usr/bin/python3
"""Rectangle module."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Checks and sets the default attributes of Rectangle class."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
