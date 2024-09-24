#!/usr/bin/python3
"""
Module base
This module contains a class Base that will
 serve as the foundation for other classes.
"""

import json


class Base:
    """
    Base class for managing 'id' attribute across all future classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance.

        Args:
            id (int, optional): assigns this value to
            the instance's id attribute.
                                Otherwise, increments the private
                                class attribute __nb_objects
                                and assigns the new value to the id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set from a dictionary."""
        inst = cls(1, 1)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                list_dicts = cls.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
