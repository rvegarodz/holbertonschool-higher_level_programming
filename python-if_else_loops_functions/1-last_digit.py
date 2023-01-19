#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = ""
num_str = repr(number)
last_digit = num_str[-1]

less_zero = "and is less than 6 and not 0"
bigger_five = "and is greater than 5"

if last_digit == "0":
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    if number < 0:
        sign = "-"
        print(f"Last digit of {number} is {sign}{last_digit} {less_zero}")
    else:
        if last_digit > "5":
            print(f"Last digit of {number} is {last_digit} {bigger_five}")
        else:
            print(f"Last digit of {number} is {sign}{last_digit} {less_zero}")
