#!/usr/bin/python3

def max_integer(my_list=[]):

    if not my_list or my_list is None:
        return (None)

    else:
        maxVal = my_list[0]

        for num in my_list:
            if num > maxVal:
                maxVal = num

        return (maxVal)
