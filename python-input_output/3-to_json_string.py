#!/usr/bin/python3
"""Module provide function called to_json_string()"""


import json


def to_json_string(my_obj):
    """Function return the JSON represantation of an object"""
    return json.dumps(my_obj)
