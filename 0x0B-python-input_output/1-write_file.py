#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Write string to a UTF8 text file.

    Args:
        filename (str): The name file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters.
    """
    with open(filename, 'w', encoding="utf-8") as myFile:
        file_det = myFile.write(text)
        return file_det
