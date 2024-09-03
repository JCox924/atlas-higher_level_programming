#!/usr/bin/python3

def uppercase(str):
    """
    :param str: string
    :return: upper case string
    """
    print("".join(chr(ord(c) - 32) if ord('a') <= ord(c) <= ord('z') else c for c in str), end="\n")
