#!/usr/bin/python3
"""Definition of a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializa new Square.

        Args:
            size (int): Size of new Square.
            x (int): x coordinate of new Square.
            y (int): y coordinate of  new Square.
            id (int): identity of  new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set size of Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attr values.
                - 1st arg repr id attr
                - 2nd arg repr size attr
                - 3rd arg repr x attr
                - 4th arg repr y attr
            **kwargs (dict): New key/value attr.
        """
        if args and len(args) != 0:
            ag = 0
            for arg in args:
                if ag == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif ag == 1:
                    self.size = arg
                elif ag == 2:
                    self.x = arg
                elif ag == 3:
                    self.y = arg
                ag += 1

        elif kwargs and len(kwargs) != 0:
            for ky, vl in kwargs.items():
                if ky == "id":
                    if vl is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = vl
                elif ky == "size":
                    self.size = vl
                elif ky == "x":
                    self.x = vl
                elif ky == "y":
                    self.y = vl

    def to_dictionary(self):
        """Return dictionary repr of Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return print() and str() repr of Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
