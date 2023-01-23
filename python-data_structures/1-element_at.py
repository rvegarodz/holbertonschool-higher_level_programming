#!/usr/bin/python3
def element_at(my_list, idx):
    len_list = len(my_list)
    
    for values in my_list:
        if idx >= 0 and idx < len_list:
            return my_list[idx]
        else:
            return None
