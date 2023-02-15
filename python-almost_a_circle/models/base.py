#!/usr/bin/python3
"""Module provide a parent class called Base"""


import json
from os import path

class Base:
    """Base class of all the other classes of the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string repr of list_dictionaries"""
        if list_dictionaries == None or list_dictionaries == {}:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Method write a JSON str repr of ist_objs to a file"""
        filename = f"{cls.__name__}" + ".json"
        tmp_lst = []
        if list_objs:
            for values in list_objs:
                tmp_lst.append(values.to_dictionary())
        with open(filename, "w") as file:
            file.write(cls.to_json_string(tmp_lst))

    @staticmethod
    def from_json_string(json_string):
        """Method returns list of the JSON str repr"""
        if json_string == None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Method that returns an instance with all attributes"""
        if cls.__name__ == "Square":
            instance = cls(1)
        elif cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        cls.update(instance, **dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """Method that returns a list of instance"""
        filename = f"{cls.__name__}" + ".json"
        if path.exists(filename) is False:
            return []
        tmp_lst = []
        with open(filename) as file:
            tmp_dict = cls.from_json_string(file.read())
            for value in tmp_dict:
                tmp_lst.append(cls.create(**value))
            return tmp_lst
