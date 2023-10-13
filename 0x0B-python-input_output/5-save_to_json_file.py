#!/usr/bin/python3
"""Defines a JSON file-writing func."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON repr."""
    with open(filename, 'w') as myFile:
        myOutput = json.dump(my_obj, myFile)
