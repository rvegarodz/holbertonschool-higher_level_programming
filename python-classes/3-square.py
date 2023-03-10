#!/usr/bin/python3
"""This module provide a class named Square"""


class Square:
    """Defines a class as Square with privates arguments (size and position).

    Args:
        param1: size

    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
