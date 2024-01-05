#!/usr/bin/python3
"""
Locked class
"""


class LockedClass:
    """
    Prevents dynamic creation of new instance
    by user
    """

    __slots__ = "first_name"
