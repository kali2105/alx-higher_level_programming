#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    count_a = tuple_a.count
    count_b = tuple_b.count
    if count_a not in range(1) or count_b not in range(1):
        tuple_a += (0, 0)
        tuple_b += (0, 0)
    sum_a = tuple_a[0] + tuple_b[0]
    sum_b = tuple_a[1] + tuple_b[1]
    new_tuple = (sum_a, sum_b)
    return new_tuple
