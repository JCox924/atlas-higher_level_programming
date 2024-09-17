#!/usr/bin/python3
"""Module contains function lookup()"""


def lookup(obj):
    """
    Function that lists the attributes and methods of an object

    :param obj: Object
    :return: list of attr and methods of an object
    """

    return dir(obj)
