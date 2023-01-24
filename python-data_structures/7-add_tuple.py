#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_copy = (0, 0)
    
    if len(tuple_a) <= 0:
        value_a = tuple_copy[0]
        value_b = tuple_copy[1]
    elif len(tuple_a) < 2:
        value_a = tuple_a[0]
        value_b = tuple_copy[1]
    else:
        value_a = tuple_a[0]
        value_b = tuple_a[1]
    if len(tuple_b) <= 0:
        value_a += tuple_copy[0]
        value_b += tuple_copy[1]
    elif len(tuple_b) < 2:
        value_a += tuple_b[0]
        value_b += tuple_copy[1]
    else:
        value_a += tuple_b[0]
        value_b += tuple_b[1]

    new_tuple = (value_a, value_b)
    return new_tuple
