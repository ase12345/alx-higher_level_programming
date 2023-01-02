#!/usr/bin/python3
"""
Module creates the Rectangle class
"""


class Rectangle:
    """
    Class Rectangle with validated private instance attributes width and height
    """

    def __init__(self, width=0, height=0):
        """Instantiates width and height using property setter
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Returns a string of Rectangle instance using #, empty string"""
        if self.width == 0 or self.height == 0:
            return ""
        row = "#" * self.width
        rect = row
        for i in range(self.height - 1):
            rect += "\n" + row
        return rect

    def __repr__(self):
        """Returns a string representation able to create new instance"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Prints 'Bye rectangle...' when instance is deleted"""
        print('Bye rectangle...')

    @property
    def width(self):
        """width: width of rectangle
        setter validates value is an integer >= 0
        Parameter:
            value: value of the width
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height: height of rectangle
        setter validates value is an integer >= 0
        Parameter:
            value: value of the height
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the calculated area of Rectangle instance"""
        return self.width * self.height

    def perimeter(self):
        """Returns the calculated perimeter of Rectangle instance"""
        if self.height == 0 or self.width == 0:
            return 0
        return (self.width + self.height) * 2
