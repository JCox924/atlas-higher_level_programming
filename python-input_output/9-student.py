# !/usr/bin/python3
"""
Module for the Student class definition.
Defines a student by first name, last name, and age,
and provides a method to retrieve the dictionary representation of a student.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
