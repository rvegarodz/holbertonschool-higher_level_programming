#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        print()
    else:
        for values in my_list[::-1]:
            print("{:d}".format(values))
