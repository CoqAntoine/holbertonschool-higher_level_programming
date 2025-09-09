#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    temp = 0
    roman_numeral = {'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1}
    if roman_string == None or not isinstance(roman_string, str):
        return 0
    for roman_letter in reversed(roman_string):
        for key, value in roman_numeral.items():
            if roman_letter == key:
                if temp > value:
                    result -= value
                else:
                    result += value
                temp = value
    return result
