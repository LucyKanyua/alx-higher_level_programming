#!/usr/bin/python3
"""Rectangle - defines a rectangle"""


class Rectangle:
    """class representation of a rectangle
        Attributes:
            __width: width of the rectangle
            __height: height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """__init__ - object constructor
            Args:
                width: optional width of the rectangle
                height: optional height of the rectangle
            Raises:
                TypeError: if width or height is not an integer
                ValueError: if width or height is less than zero
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter for property width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width
            Args:
                value: the new value for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for property height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height
            Args:
                value: the new value for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
