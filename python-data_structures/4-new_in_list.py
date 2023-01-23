#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return
    else:
        len_list = len(my_list)
        for values in my_list:
            if idx < 0:
                return my_list
            elif idx > 0:
                copy_list = my_list.copy()
                if idx < len_list:
                    copy_list[idx] = element
                return copy_list
