#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for key, value in a_dictionary.items():
        new_dictionary[key] = value * value
    return new_dictionary
