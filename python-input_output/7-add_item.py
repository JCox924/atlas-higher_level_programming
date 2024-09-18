#!/usr/bin/python3
"""module docstring"""
import sys
import os
import json


def save_to_json_file(my_obj, filename):
    """Saves an object to a text file using JSON representation."""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """Loads an object from a text file using JSON representation."""
    with open(filename, 'r') as f:
        return json.load(f)


filename = "add_item.json"

try:
    if os.path.exists(filename):
        items = load_from_json_file(filename)
    else:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
