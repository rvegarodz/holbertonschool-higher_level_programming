#!/usr/bin/python3
"""This module provide a new class called MyList"""


class MyList(list):
    """Defines a new class MyList that inherits from list"""
    def print_sorted(self):
        list = []
        for value in self:
            list.append(value)
        list.sort()
        print(list)
