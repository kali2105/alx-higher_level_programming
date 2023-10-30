#!/usr/bin/python3
def add_integer(a, b=98):
    ''' addition function 
    if type(a) is int:
        if type(b) is int:
            return a + b
        elif type(b) is float:
            return a + int(b)
        else:
            raise TypeError("b must be an integer")
    elif type(b) is float:
        if type(b) is int:
            return int(a) + b
        elif type(b) is float:
            return int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")'''
    num_type = [int, float]
    if type(a) not in num_type:
        raise TypeError("a must be an integer")
    elif type(b) not in num_type:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
