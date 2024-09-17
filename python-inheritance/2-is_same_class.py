#!/usr/bin/python3
"""Module defines is_same_class()"""


def is_same_class(obj, a_class) -> bool:
    """
    :param obj: object instance to check
    :param a_class: class to check
    :return True: if the object is exactly an
        instance of the specified class
    :return False: other
    """

    return type(obj) is a_class
