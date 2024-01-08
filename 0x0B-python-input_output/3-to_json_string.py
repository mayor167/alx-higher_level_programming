#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return JSON repr of string object."""
    serialize = json.dumps(my_obj)
    return serialize
