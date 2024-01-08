#!/usr/bin/python3
"""
1-my_list.py

features MyList class that inherits from list
contains public instance method to print ascended sorted list
"""


class MyList(list):
    """inherits from list"""

    def print_sorted(self):
        """prints sorted list of ints in ascending order"""
        print(sorted(self))
