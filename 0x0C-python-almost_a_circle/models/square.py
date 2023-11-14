#!/usr/bin/python3
"""class Rectangle that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Rectangle that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor. Self.width and self.height are both set to size """
        super().__init__(size, size, x, y, id)
        self.x = x
        self.y = y

    @property
    def size(self):
        """Getter for width and height that inherits that of Rectangle"""
        return self.width  # Or return self.height here #

    @size.setter
    def size(self, value):
        """Setter for height/width"""
        self.width = value
        self.height = value

    def __str__(self):
        """ Overloading __str__ method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """Assigns attributes to each attribute"""
        argmnts = ('id', 'size', 'x', 'y')

        if args:
            for i, value in enumerate((args)):
                setattr(self, argmnts[i], value)

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary represenatation of Square"""
        return{key: getattr(self, key) for key in ('id', 'size', 'x', 'y')}
