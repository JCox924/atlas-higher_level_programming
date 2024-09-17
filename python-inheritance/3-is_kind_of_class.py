#!/usr/bin/python3

def is_kind_of_class(obj, a_class) -> bool:
    """
    is_kind_of_class

    :param obj:
    :param a_class:
    :return: True if object instance is an instance of a_class
    """

    return type(obj) is a_class
