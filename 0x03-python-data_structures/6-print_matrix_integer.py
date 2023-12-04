#!/usr/bin/python3

def print_matrix_integer(matrix=None):
    if matrix is None:
        return

    for row in matrix:
        for col_index, element in enumerate(row):
            print("{:d}".format(element), end="")
            if col_index != len(row) - 1:
                print(" ", end="")
        print("")
