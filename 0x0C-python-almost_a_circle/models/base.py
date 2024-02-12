#!/usr/bin/python3

import json
import os.path


class Base:
    """Base model
    This Represents the "base" for all other classes in project 0x0c*

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance.
        Args:
            id (int, optional): The identifier of the instance.
            If None, a unique identifier will be assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def create(cls, **dictionary):
        """Create an instance of the class using a dictionary of attributes.

         Args:
            dictionary (dict): The dictionary containing attribute values.

        Returns:
            Base: An instance of the class.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): The list of dictionaries to convert.

        Returns:
            str: The JSON string.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of instances to a JSON file.

        Args:
            list_objs (list): The list of instances to save.
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): The JSON string to convert.

        Returns:
            list: The list of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file.

        Returns:
                   list: The list of instances loaded from the file.
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []

        with open(filename, "r") as file:
            json_data = file.read()
            dictionaries = cls.from_json_string(json_data)
            instances = [cls.create(**dictionary) for dictionary in dictionaries]
            return instances

