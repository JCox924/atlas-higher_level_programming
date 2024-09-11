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
    
    for char in text:
        new_text += char
        if char in characters:
            new_text += "\n\n"

    new_text = new_text.strip()

    lines = new_text.splitlines()
    for line in lines:
        print(line.strip())
