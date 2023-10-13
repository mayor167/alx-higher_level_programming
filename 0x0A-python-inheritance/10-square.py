#!/usr/bin/python3
"""Square module."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Checks and sets the default attributes of Square class."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
