#!usr/bin/python3
"""Module contains function class_to_json()"""

def class_to_json(obj):
    """
    Function that returns the dictionary description with simple data structure (list, dictionary,
    string, integer and boolean) for JSON serialization of an object
    :param obj: an instance of a Class
    :return: dictionary
    """
    return obj.__dict__
