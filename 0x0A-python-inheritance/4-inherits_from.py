#!/usr/bin/python3
"""inherits_from module."""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a
    class inherited
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
