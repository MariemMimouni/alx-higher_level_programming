#!/usr/bin/python3
"""Define a square."""


class Square:
    """ Represent a square."""
    def __init__(self, size=0):
        """Initialize a square
        args: size = 0"""
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns square area
        args: self"""
        return self.__size*self.__size

    @property
    def size(self):
        """ Retrieve __size"""
        return self.__size

    @size.setter
    def size(self, size):
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
