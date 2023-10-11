#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for i in my_list:
        sum += i / my_list.count(i)
    return int(sum)
