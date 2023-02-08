#!/usr/bin/python3
"""COMMENT"""


def is_same_class(obj, a_class):
    """COMMENT"""
    if a_class is not object:
        if isinstance(obj, a_class) is True:
            return True
        else:
            return False
    else:
        return False