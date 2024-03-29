#!/usr/bin/python3
""" Represent a rectangle as a class"""


class Rectangle:
    """ Define a rectangle"""

    @property
    def width(self):
        """Retrieve width """
        return self.__width

    @width.setter
    def width(self, value):
        """Set width value"""
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height value"""
        if not(isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __init__(self, width=0, height=0):
        """Initialize rectangle
        args: width = 0
        height = 0"""
        self.width = width
        self.height = height
