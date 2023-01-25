#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list[:])
    product = 0
    for value in my_set:
        product += value
    return product
