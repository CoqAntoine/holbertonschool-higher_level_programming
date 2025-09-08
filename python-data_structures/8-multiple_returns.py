#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if len(sentence) == 0:
        first_letter = None
    else:
        first_letter = sentence[0]
    result = length, first_letter
    return result
