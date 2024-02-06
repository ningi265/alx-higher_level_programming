#!/usr/bin/python3
"""Script to add command-line arguments to a JSON file."""

import sys

if __name__ == "__main__":
    # Importing functions for saving and loading JSON files
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        # Attempting to load data from an existing JSON file
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # If the file doesn't exist, initializing an empty list
        items = []

    # Appending command-line arguments to the list
    items.extend(sys.argv[1:])

    # Saving the updated list to the JSON file
    save_to_json_file(items, "add_item.json")

