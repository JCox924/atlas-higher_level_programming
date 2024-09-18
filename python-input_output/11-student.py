# !/usr/bin/python3
"""
This module defines a Student class, which provides a way to store and manipulate student data.

The Student class includes:
- Public instance attributes: first_name, last_name, age
- An initializer method for instantiation
- A method for retrieving a dictionary representation of the instance
- A method for updating the instance attributes from a dictionary
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        return {attr: self.__dict__.get(attr) for attr in attrs if attr in self.__dict__}

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
