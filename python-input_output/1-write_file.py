#!/usr/bin/python3
""" Module provide a function called write_file()"""


def write_file(filename="", text=""):
    """ Function that writes a str to a txt file, return lenght of str"""
    with open(filename, "w+", encoding="utf-8") as file:
        return file.write(text)
