#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    new_list = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            new_list += 1
    except (IndexError, TypeError):
        pass
    print()
    return new_list
