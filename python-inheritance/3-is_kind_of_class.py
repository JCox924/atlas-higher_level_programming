#!/usr/bin/python3
"""Module defines is_kind_of_class()"""


def is_kind_of_class(obj, a_class) -> bool:
    """
    is_kind_of_class

    :param obj: object
    :param a_class: class
    :return: True if object instance is an instance of a_class
    """

    return type(obj) is a_class
