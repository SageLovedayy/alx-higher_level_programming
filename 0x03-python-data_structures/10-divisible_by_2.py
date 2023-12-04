#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    boolList = []
    for num in my_list:
        boolList.append(num % 2 == 0)

    return (boolList)
