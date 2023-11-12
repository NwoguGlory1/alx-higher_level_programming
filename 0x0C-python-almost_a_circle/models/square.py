#!/usr/bin/python3
"""class Rectangle that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Rectangle that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor"""
        super().__init__(size, size, x, y, id)
        """self.width and self.height are both set to size in super init"""
        self.x = x
        self.y = y

    def size(self):
        """ width and height that inherits that of Rectangle"""
        return self.size

    def __str__(self):
        """ Overloading __str__ method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
