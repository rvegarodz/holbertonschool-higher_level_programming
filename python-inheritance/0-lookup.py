#!/usr/bin/python3
"""This module provide a function called lookup"""


def lookup(obj):
    """Function that returns list with attributes and methods of obj"""
    new_list = dir(obj)
    return new_list
