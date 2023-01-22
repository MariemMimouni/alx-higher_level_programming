#!/usr/bin/python3
"""Define a square."""


class Square:
    """ Represent a square."""

    @property
    def size(self):
        """ Retrieve __size"""
        return self.__size

    @size.setter
    def size(self, size):
        """set size"""
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """Retrieve __position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set position"""
        if not (isinstance(value, tuple)
                and len(value) == 2
                and isinstance(value[0], int)
                and isinstance(value[1], int)
                and value[0] >= 0
                and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square
        args: size = 0
        position =(0, 0)"""
        self.size = size
        self.position = position

    def my_print(self):
        """Prints the square in #"""
        if self.__size == 0:
            print()
            return
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    def area(self):
        """Returns square area
        args: self"""
        return self.__size*self.__size
