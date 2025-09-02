#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    add = 0

    if argc == 0:
        add = 0
    elif argc == 1:
        add = int(argv[1])
    else:
        for i in range(1, argc + 1):
            add = add + int(argv[i])
    print("{}".format(add))
