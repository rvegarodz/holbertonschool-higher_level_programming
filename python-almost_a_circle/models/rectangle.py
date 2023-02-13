#!/usr/bin/python3
"""Module provide a Rectangle Class that inherits from Base"""


from models.base import Base

class Rectangle(Base):
    """Create Rectangle class that inherits from Base class"""


    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
