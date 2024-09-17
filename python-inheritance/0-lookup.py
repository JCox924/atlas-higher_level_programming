#!/usr/bin/python3

def lookup(obj):
    """
    Function that lists the attributes and methods of an object

    :param obj: Object
    :return: list of attr and methods of an object
    """

    return dir(obj)
