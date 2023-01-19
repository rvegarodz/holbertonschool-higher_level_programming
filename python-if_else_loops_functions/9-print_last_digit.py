#!/usr/bin/python3
def print_last_digit(number):
    num_str = repr(number)
    last_digit = num_str[-1]

    print(last_digit, end="")
    return last_digit

r = print_last_digit(98)
print(r)