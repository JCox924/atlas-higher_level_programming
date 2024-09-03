#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = []
    for element in my_list:
        if element not in unique_integers:
            unique_integers.append(element)
    return sum(unique_integers)
