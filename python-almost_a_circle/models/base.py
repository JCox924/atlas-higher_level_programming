#!/usr/bin/python3
"""
Module base
This module contains a class Base that will
 serve as the foundation for other classes.
"""


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
