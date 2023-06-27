#!/usr/bin/python3
"""Square: This module contains the definition of class Square"""


class Square:
    """ A class efining a square
    Methods:
    __set_size: validates argument size and initializes __size
    area: calculates the area of the square"""
    def __init__(self, size=0):
        """ Parameters:
        size:(optional) length of one sie of the square"""
        self.__set_size(size)

        def __set_size(self, size):
            """ Initializes the attribut __size
            Parameters:
            size: valu for initializing __size"""
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("siz must be >= 0")
            else:
                self.__size = size

                def area(self):
                    """ area: calculates and returns the area of the square."""
                    return self.__size * self.__size
