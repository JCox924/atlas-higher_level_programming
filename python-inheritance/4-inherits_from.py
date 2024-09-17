#!/usr/bin/python3
"""Module defines inherits_from()"""


def inherits_from(obj, a_class) -> bool:
    """
    inherits_from

    :param obj: object
    :param a_class: class
    :return: True if object inherits from a_class
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
