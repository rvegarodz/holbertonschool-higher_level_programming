#!/usr/bin/python3
"""Module provide a Rectangle Class that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """Create Rectangle class that inherits from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        else:
            if height <= 0:
                raise ValueError("height must be > 0")
            self.__height = height
        if type(x) != int:
            raise TypeError("x must be an integer")
        else:
            if x < 0:
                raise ValueError("x must be >= 0")
            self.__x = x
        if type(y) != int:
            raise TypeError("y must be an integer")
        else:
            if y < 0:
                raise ValueError("y must be >= 0")
            self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        else:
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        else:
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        else:
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

    def area(self):
        """Area method return the area of the Rectangle"""
        return self.__height * self.__width

    def display(self):
        """Display method print the rectangle dimensions with #"""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """Magic method that return string"""
        __id_msg = (f"({self.id})")
        __x_y_msg = (f"{self.x}/{self.y}")
        __w_h_msg = (f"{self.__width}/{self.__height}")
        return f"[Rectangle] {__id_msg} {__x_y_msg} - {__w_h_msg}"
