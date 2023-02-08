#!/usr/bin/python3
"""This module provide a class named Rectangle"""

def lookup(obj):
    """Function that returns the list of available attributes and methods of obj"""
    new_list = []
    new_list.append(dir(obj))
    return new_list
