#!/usr/bin/python3
"""A magicClass python"""
import math


class MagicClass:
    """This represents a circle"""
    def __init__(self, radius=0):
        """Initializes the Magic Class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """A function that calculaes the area of the circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """A function that calculates the circumference of the circle"""
        return 2 * math.pi * self.__radius
