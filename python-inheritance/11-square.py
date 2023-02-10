#!/usr/bin/python3
"""comment"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """comment"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return f'[Square] {self.__size}/{self.__size}'
