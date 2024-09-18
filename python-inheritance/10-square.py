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

    def area(self):
        """Calculates the area of the rectangle

        Returns:
            int: The area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the rectangle

        Returns:
            str: Rectangle description in the format [Rectangle] <width>/<height>
        """

        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize the square with size

        Args:
            size (int): The size of the square, must be validated.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """Returns the string representation of the square

        Returns:
            str: Square description in the format [Square] <size>/<size>
        """
        return f"[Square] {self.__size}/{self.__size}"
