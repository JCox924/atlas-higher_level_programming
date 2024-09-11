#!/usr/bin/python3
"""
Module text_indentation
Defines a function to print a text with
2 new lines after each of these characters: ., ? and :.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): The text to be processed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in characters:
            print("\n")
            i += 1

            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
