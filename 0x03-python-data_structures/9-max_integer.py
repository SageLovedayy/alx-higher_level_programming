#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        maxVal = my_list[0]

        for num in my_list:
            if num > maxVal:
                maxVal = num

        return (maxVal)

    else:
        return (None)


print(max_integer([15, 15, 8]))
