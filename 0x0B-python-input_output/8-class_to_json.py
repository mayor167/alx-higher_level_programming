#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary repr of data structure."""
    serialized_items = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (int, bool, str, dict, list)):
            serialized_items[key] = value
    return serialized_items
