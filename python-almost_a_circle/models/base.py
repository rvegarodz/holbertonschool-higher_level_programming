#!/usr/bin/python3
"""Module provide a parent class called Base"""


import json

class Base:
    """Base class of all the other classes of the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
        
    def to_json_string(list_dictionaries):
        """Returns the JSON string repr of list_dictionaries"""
        return json.dumps(list_dictionaries)