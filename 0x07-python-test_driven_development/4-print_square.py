#!/usr/bin/python3
"""has a function that prints a square with the character '#'"""


def print_square(size):
    """prints a square of length 'size'
        Args:
            size: length and width of square to print
        Raises:
            TypeError: - if size of the square is not an integer
                        - if size is a float and is less than zero
            ValueError: if size is less than 0
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for n in range(size):
        for l in range(size):
            print("#", end="")
        print()
