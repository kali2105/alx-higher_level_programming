#!/usr/bin/python3
"""A square class"""


class Square:
    """Comment on Square class
    Attributes:
        __size (int): size of the square
    """
    def __init__(self, size=0):
        """Initializing a square class
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        self.__size = size
        if type(size) == int:
            if size < 0:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
        The area of square
        Return:
            return the ara of the square
        """

        return self.__size ** 2
