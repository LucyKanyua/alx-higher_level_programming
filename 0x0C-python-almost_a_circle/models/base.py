#!/usr/bin/python3
"""Defines Base class for ll the classes in the Almost_a_circle project"""


import csv
import json


class Base:
    """Base class for all the classes and manages the id attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes the id attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
