#!/usr/bin/python3
def print_last_digit(number):
    if number <= 0 or number >= 0:
        num_str = repr(number)
        last_digit = num_str[-1]
        print(last_digit, end="")
        return last_digit
