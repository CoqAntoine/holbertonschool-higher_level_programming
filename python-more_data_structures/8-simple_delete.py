#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        temp = {k: v for k, v in a_dictionary.items() if k != key}
        a_dictionary.clear()
        a_dictionary.update(temp)
    return a_dictionary
