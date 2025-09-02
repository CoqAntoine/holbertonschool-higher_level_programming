#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 'a' <= i <= 'z':
            print("{:c}".format(ord(i) - 32), end='')
        else:
            print("{:c}".format(ord(i)), end='')
    print()
