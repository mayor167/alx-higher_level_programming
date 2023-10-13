#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from JSON file."""
    with open(filename, 'r') as myFile:
        read_line = json.load(myFile)
        return read_line

