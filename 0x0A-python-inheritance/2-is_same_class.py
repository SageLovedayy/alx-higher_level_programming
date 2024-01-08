#!/usr/bin/python3
"""
Exact same object

checks if an object is exactly an instance of a given class
"""


def is_same_class(obj, a_class):
    """returns True if object is exact instance of specified class"""

    return (type(obj) is a_class)
