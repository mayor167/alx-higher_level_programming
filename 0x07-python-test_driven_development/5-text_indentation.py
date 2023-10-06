#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """ text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    ct = 0
    while ct < len(text) and text[ct] == ' ':
        ct += 1

    while ct < len(text):
        print(text[ct], end="")
        if text[ct] == "\n" or text[ct] in ".?:":
            if text[ct] in ".?:":
                print("\n")
            ct += 1
            while ct < len(text) and text[ct] == ' ':
                ct += 1
            continue
        ct += 1