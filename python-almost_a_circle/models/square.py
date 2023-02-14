#!/usr/bin/python3
"""Module provide a subclass Square that inherits from Rectangle"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """Create Square class that inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"