#!/usr/bin/python3
"""write_file module."""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file"""
    put = ""
    with open(filename, 'r') as file:
        for lines in file:
            put += lines
            if search_string in lines:
                put += new_string

    with open(filename, 'w') as file:
        file.write(put)
