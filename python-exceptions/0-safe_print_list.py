#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for value in range(x):
            print("{}".format(my_list[value]), end="")
        print()
        return x
    except IndexError:
        idx = 0
        for value in my_list:
            if idx == x:
                break
            else:
                idx += 1
        print()
        return idx