#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    i = len(argv) - 1
    sum = 0

    while (i > 0):
        sum += int(argv[i])
        i -= 1

    print(sum)
