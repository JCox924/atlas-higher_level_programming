#!/usr/bin/python3

def uppercase(str):
    """
    uppercase(str: string)
    :param str: string
    :return: string in caps
    """
    result = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            result += "{:c}".format(ord(char) - 32)
        else:
            result += "{:c}".format(ord(char))
    print(result)
