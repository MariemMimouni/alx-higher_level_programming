#!/usr/bin/python3
""" Represent a rectangle as a class"""


class Rectangle:
    """ Define a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    def area(self):
        """ Returns area of rectangle"""
        return (self.__width*self.__height)

    def perimeter(self):
        """Returns perimeter of recatngle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width + self.__height)*2

    def __str__(self):
        """print() and str()"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    print(str(self.print_symbol), end="")
                if i != self.__height - 1:
                    print()
            return ""

    def __repr__(self):
        """repr() a rectangle"""
        r = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return r

    def __del__(self):
        """Called when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not (isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not (isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if (rect_1.area() > rect_2.area()):
                return rect_1
            elif (rect_1.area() < rect_2.area()):
                return rect_2
            else:
                return rect_1
