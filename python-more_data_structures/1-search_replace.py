#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_copy = my_list[:]
    for idx, value in enumerate(list_copy):
        if value == search:
            list_copy[idx] = replace
    return list_copy
