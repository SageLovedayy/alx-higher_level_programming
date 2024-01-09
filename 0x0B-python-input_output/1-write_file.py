#!/usr/bin/python3

"""Write to file Module"""


def write_file(filename="", text=""):
    """
    writes a string to a text file
    Return: number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        return (file.write(text))
