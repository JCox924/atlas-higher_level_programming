#!/usr/bin/python3
"""
Module square
This module contains class Square.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    A Square is a rectangle where the width and height are equal.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square
            x (int, optional): The x-coordinate of the square
            y (int, optional): The y-coordinate of the square
            id (int, optional): The id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieve the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square, assigning it to both width and height.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes using *args or **kwargs.

        Args:
            1st argument: id
            2nd argument: size
            3rd argument: x
            4th argument: y
        """
        if args and len(args) > 0:
            attributes = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __str__(self):
        """return the string representation of the Square instance."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """Return dictionary representation of Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
