#!usr/bin/python3
"""
1-Base class module
"""


class Base:
    """
    base class of other classes
    For managing id attribute in all future classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb.objects