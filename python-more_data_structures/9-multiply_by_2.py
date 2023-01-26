#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy_dictionary = a_dictionary.copy()
    keys_a = list(copy_dictionary.keys())
    keys_a.sort()
    for keys in keys_a:
        value = copy_dictionary[keys]
        copy_dictionary[keys] = value * 2
    return copy_dictionary