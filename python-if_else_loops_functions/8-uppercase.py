#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if 'a' <= i <= 'z':
            result += "{:c}".format(ord(i) - 32)
        else:
            result += "{:c}".format(ord(i))
    print(result)