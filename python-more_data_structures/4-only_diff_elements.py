#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set_1.union(set_2)
    for value in set_1:
        for value2 in set_2:
            if value == value2:
                new_set.remove(value)
    return new_set
