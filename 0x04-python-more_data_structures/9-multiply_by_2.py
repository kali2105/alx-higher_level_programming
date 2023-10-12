#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mult_dic = {}
    for key, value in a_dictionary.items():
        mult_dic[key] = value * 2
    return mult_dic
