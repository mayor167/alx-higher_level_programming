#!/usr/bin/python3
"""Defines JSON-to-object func."""
import json


def from_json_string(my_str):
    """Return the Python object repr of JSON string."""
    loaded = json.loads(my_str)
    return loaded
