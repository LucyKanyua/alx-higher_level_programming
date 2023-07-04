#!/usr/bin/python3
"""say_my_name - has a  function that prints out my name"""


def say_my_name(first_name, last_name=""):
    """prints out first_name last_name
        Args:
            first_name: first name
            last_name: last name
        Raises:
            TypeError: if either first_name or last_name are not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("{} {}".format(first_name, last_name))
