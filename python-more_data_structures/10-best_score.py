#!/usr/bin/python3
def best_score(a_dictionary):
    name = None
    best_score = 0
    if bool(a_dictionary):
        for key, value in a_dictionary.items():
            if value > best_score:
                best_score = value
                name = key
    return name
