#!/usr/bin/python3
""" This module provide a function called read_file"""


def read_file(filename=""):
    """ Function that print content of a file

        Args:
        filename: name of the file to read
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read())
