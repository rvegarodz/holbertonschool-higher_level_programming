#!/usr/bin/python3
"""comment"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """comment"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self._Square__size = size
        
    def __str__(self):
        return ("[Square] {}/{}".format(self._Square__size, self._Square__size))