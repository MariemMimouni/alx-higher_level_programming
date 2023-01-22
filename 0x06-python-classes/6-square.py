#!/usr/bin/python3
"""Define a square."""


class Square:
    """ Represent a square."""
    def __init__(self, size=0, position(0, 0)):
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

    def my_print(self):
        """Prints the square in #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for y in range(self.__position[1]):
                    print()
                for j in range(self.__size):
                    for x in range(self.__position[0]):
                        print(" ", end="")
                    print("#", end="")
                print()

    @property
    def position(self):
        """Retrieve __position"""
        return ___self.position

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple) and len(value) == 2 and value[0] > 0 and value[1] > 0):
            raise TypeError("position must be a tuple of 2 positive integers")
