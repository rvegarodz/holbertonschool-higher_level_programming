#!/usr/bin/python3
value = 0
for value in range(99):
    hexa = hex(value)
    str = "{} = {}"
    print(str.format(value, hexa))
