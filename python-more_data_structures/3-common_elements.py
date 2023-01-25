#!/usr/bin/python3
def common_elements(set_1, set_2):
    my_list = []
    for value in set_1:
        for value2 in set_2:
            if value == value2:
                my_list.append(value)
    return set(my_list)
