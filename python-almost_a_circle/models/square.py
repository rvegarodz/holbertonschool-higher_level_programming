#!/usr/bin/python3
"""Module provide a subclass Square that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Create Square class that inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value

    def update(self, *args, **kwargs):
        """Method that update arguments of class"""
        if args:
            for idx in range(len(args)):
                if idx == 0:
                    self.id = args[idx]
                if idx == 1:
                    super(__class__, self.__class__).
                    width.__set__(self, args[idx])
                if idx == 2:
                    super(__class__, self.__class__).
                    x.__set__(self, args[idx])
                if idx == 3:
                    super(__class__, self.__class__).
                    y.__set__(self, args[idx])
        else:
            for value in kwargs:
                if value == "id":
                    self.id = kwargs[value]
                if value == "size":
                    super(__class__, self.__class__).
                    width.__set__(self, kwargs[value])
                if value == "x":
                    super(__class__, self.__class__).
                    x.__set__(self, kwargs[value])
                if value == "y":
                    super(__class__, self.__class__).
                    y.__set__(self, kwargs[value])

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """Funtion returns the dict repr of a Square"""
        return {"id": self.id, "x": self.x, "size": self.width, "y": self.y}
