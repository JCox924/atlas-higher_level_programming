#!/usr/bin/python3
"""Module contains class Rectangle"""


class BaseGeometry:
    """Class for geometry objects"""

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer greater than 0"""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize the rectangle with width and height

        Args:
            width (int): The width of the rectangle, must be validated.
            height (int): The height of the rectangle, must be validated.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
