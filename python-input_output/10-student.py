# !/usr/bin/python3
"""
This module defines a class Student that defines a student by:
- Public instance attributes: first_name, last_name, age
- Instantiation with first_name, last_name, and age
- Method to_json that retrieves a dictionary representation of a Student instance
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            return {key: self.__dict__[key] for key in attrs if key in self.__dict__}
