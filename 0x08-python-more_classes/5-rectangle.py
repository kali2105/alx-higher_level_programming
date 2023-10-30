#!/usr/bin/python3
'''This function define a rectangle by private instance attribute'''


class Rectangle:
    '''The __init__ method initialize the values passed to the object
    Attributes:
        width: A private width attribute.
        height: A private height attribute.
    '''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        '''The width properties'''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''The height properties'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        rectangle = ''
        for row in range(self.__height):
            for column in range(self.__width):
                rectangle += '#'
            if row < self.__height - 1:
                rectangle += '\n'
        return rectangle

    def __repr__(self):
        return ("Rectangle(" + str(self.width) + ", " + str(self.height) + ")")

    def __del__(self):
        print("Bye rectangle...")
