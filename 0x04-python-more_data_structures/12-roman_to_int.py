#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    rm_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rm_i = 0
    for j in range(len(roman_string)):
        if j > 0 and rm_d[roman_string[j]] > rm_d[roman_string[j - 1]]:
            rm_i += rm_d[roman_string[j]] - 2 * \
                    rm_d[roman_string[j - 1]]
        else:
            rm_i += rm_d[roman_string[j]]
    return rm_i
