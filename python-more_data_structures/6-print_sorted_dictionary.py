#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_keys = list(a_dictionary.keys())
    dict_keys.sort()
    for keys in dict_keys:
        print("{}: {}".format(keys, a_dictionary.get(keys)))
