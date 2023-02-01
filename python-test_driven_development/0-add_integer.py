#!/usr/bin/python3
"""This module provide a function called add_integer()"""


def add_integer(a, b=98):
    """This function sum 2 values
    Args:
        a: integer or float value
        b: integer or float value
    Return:
        The return value is the sum of a and b
    Raises:
        TypeError: If a or b are not integer or float

    """
    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
    if type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
