#!/usr/bin/python3
"""Module provide a function called append_write()"""


def append_write(filename="", text=""):
    """Function that appends a str at the end of a txt file,
    return lenght of str"""
    open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
