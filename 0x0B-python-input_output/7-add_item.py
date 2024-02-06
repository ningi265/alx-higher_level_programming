#!/usr/bin/python3
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file
import sys

def add_arguments_to_list(args):
    """
    Adds command-line arguments to a Python list and saves the list to a file.

    Args:
        args (list): A list of command-line arguments.

    Returns:
        None
    """
    try:
        # Load existing items from file if it exists
        try:
            items = load_from_json_file("add_item.json")
        except FileNotFoundError:
            items = []

        # Add new items from command-line arguments
        items.extend(args)

        # Save the updated list to file
        save_to_json_file(items, "add_item.json")
        print("Items added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ignore the script name (first argument)
    args = sys.argv[1:]
    if args:
        add_arguments_to_list(args)
    else:
        print("No items provided.")

