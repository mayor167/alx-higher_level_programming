#!/usr/bin/python3
"""Defines an inherited list class."""


class MyList(list):
    """sorted printing for built-in list class."""

    def print_sorted(self):
        """Print list in sorted ascending order."""
        print(sorted(self))
