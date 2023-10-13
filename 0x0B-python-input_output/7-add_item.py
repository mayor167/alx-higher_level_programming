#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import json


def save_to_json_file(my_obj, filename):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(my_obj, file)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def load_from_json_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            loaded_obj = json.load(file)
            return loaded_obj
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
