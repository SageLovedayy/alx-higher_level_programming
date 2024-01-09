#!/usr/bin/python3

"""Read file module"""


def read_file(filename=""):
    """reads and prints a text file to stdout"""
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
