#!/usr/bin/python3

class MyList(list):
    """
    A subclass of list with a method to
    print the list sorted in
    ascending order
    """

    def print_sorted(self):
        """prints list in ascending order"""
        print(sorted(self))
