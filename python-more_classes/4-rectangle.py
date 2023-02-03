#!/usr/bin/python3
"""This module provide a class named Square"""


class Rectangle:
    """Defines a class as Square with privates arguments (size and position).

    Args:
        param1: width
        param2: height

    """
    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        _area = self.__height * self.__width
        return _area

    def perimeter(self):
        if self.__height != 0 and self.__width != 0:
            _perimeter = (self.__height * 2) + (self.__width * 2)
        else:
            _perimeter = 0
        return _perimeter

    def __str__(self):
        str_rep = ""
        if self.__height != 0 and self.__width != 0:
            for i in range(self.__height):
                if i != 0:
                    str_rep += "\n"
                for j in range(self.__width):
                    str_rep += "#"
        return str_rep

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
