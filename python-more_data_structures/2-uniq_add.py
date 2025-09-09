#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    verification_list = []
    for i in my_list:
        if i not in verification_list:
            verification_list.append(i)
            result += i
    return(result)
