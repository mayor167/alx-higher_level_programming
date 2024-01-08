#!/usr/bin/python3
"""file-appending function."""


def append_write(filename="", text=""):
    """Appends string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, 'a', encoding="utf-8") as myFile:
        file_cont = myFile.write(text)
        return file_cont
