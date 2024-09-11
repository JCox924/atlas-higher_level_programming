#!/usr/bin/python3
"""
Module text_indentation
Defines a function to print a text with 2 new lines after each of these characters: ., ? and :.
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
    new_text = ""

    i = 0
    while i < len(text):
        new_text += text[i]
        if text[i] in characters:
            new_text += "\n\n"

            while i + 1 < len(text) and text[i + 1] == "":
                i += 1
        i += 1

    new_text = new_text.strip()


    lines = new_text.splitlines()
    for line in lines:
        print(line.strip())
