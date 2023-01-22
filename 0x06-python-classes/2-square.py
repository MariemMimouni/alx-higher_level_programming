#!/usr/bin/python3
"""Define a square."""


class Square:
    """ Represent a square."""
    def __init__(self, size=0):
        """Initialize a square
        args: size = 0"""
        if size < 0:
            raise ValueError("size must be >= 0")
        if not (type(size) == int):
            raise TypeError("size must be an integer")
        self.__size = size
