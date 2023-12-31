#!/usr/bin/python3
"""class Rectangle that inherits from Base"""

from models.base import Base
""" import Base"""


class Rectangle(Base):
    """ define Inherited Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializer
        Args:
            width: the width value
            height: the height value
            x: x value
            y: y value
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """public method that returns the area of Rectangle instance"""
        return (self.__width * self.__height)

    def display(self):
        """pubic method tha prints in stdout Rectangle instance with: # """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(' ', end='')
            for k in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """Overriding the __str__ method"""
        xy = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        xy = xy.format(self.id, self.x, self.y, self.width, self.height)
        return xy

    def update(self, *args, **kwargs):
        """Assigns arguments to each attribute"""
        argmnts = ('id', 'width', 'height', 'x', 'y')

        if args:
            for i, value in enumerate((args)):
                setattr(self, argmnts[i], value)

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dict representation aof a Rectangle"""
        yz = ('id', 'width', 'height', 'x', 'y')
        return{key: getattr(self, key) for key in (yz)}
