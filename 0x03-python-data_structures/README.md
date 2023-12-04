# Higher Level Programming - Python Data Structures

This repository contains Python scripts demonstrating various tasks related to data structures.

## Table of Contents

1. [Print a list of integers](./0x03-python-data_structures/0-print_list_integer.py)
2. [Secure access to an element in a list](./0x03-python-data_structures/1-element_at.py)
3. [Replace element in a list](./0x03-python-data_structures/2-replace_in_list.py)
4. [Print a list of integers in reverse](./0x03-python-data_structures/3-print_reversed_list_integer.py)
5. [Replace in a copy](./0x03-python-data_structures/4-new_in_list.py)
6. [Remove characters 'c' and 'C' from a string](./0x03-python-data_structures/5-no_c.py)
7. [Print a matrix of integers](./0x03-python-data_structures/6-print_matrix_integer.py)
8. [Add two tuples](./0x03-python-data_structures/7-add_tuple.py)
9. [Multiple returns](./0x03-python-data_structures/8-multiple_returns.py)
10. [Find the max integer in a list](./0x03-python-data_structures/9-max_integer.py)
11. [Check if integers in a list are divisible by 2](./0x03-python-data_structures/10-divisible_by_2.py)
12. [Delete an element at a specific position in a list](./0x03-python-data_structures/11-delete_at.py)
13. [Switch values of two variables](./0x03-python-data_structures/12-switch.py)
14. [Check if a linked list is a palindrome](./0x03-python-data_structures/13-is_palindrome.c)

## Description

### 0. Print a list of integers
- **File:** [0-print_list_integer.py](./0x03-python-data_structures/0-print_list_integer.py)
- **Description:** This script defines a function `print_list_integer(my_list)` that prints all integers of a given list, with one integer per line.

### 1. Secure access to an element in a list
- **File:** [1-element_at.py](./0x03-python-data_structures/1-element_at.py)
- **Description:** This script defines a function `element_at(my_list, idx)` that retrieves an element from a list. If the index is negative or out of range, it returns `None`.

### 2. Replace element in a list
- **File:** [2-replace_in_list.py](./0x03-python-data_structures/2-replace_in_list.py)
- **Description:** This script defines a function `replace_in_list(my_list, idx, element)` that replaces an element in a list at a specific position. If the index is negative or out of range, it returns the original list.

### 3. Print a list of integers in reverse
- **File:** [3-print_reversed_list_integer.py](./0x03-python-data_structures/3-print_reversed_list_integer.py)
- **Description:** This script defines a function `print_reversed_list_integer(my_list)` that prints all integers of a given list in reverse order, with one integer per line.

### 4. Replace in a copy
- **File:** [4-new_in_list.py](./0x03-python-data_structures/4-new_in_list.py)
- **Description:** This script defines a function `new_in_list(my_list, idx, element)` that replaces an element in a list at a specific position without modifying the original list. If the index is negative or out of range, it returns a copy of the original list.

### 5. Remove characters 'c' and 'C' from a string
- **File:** [5-no_c.py](./0x03-python-data_structures/5-no_c.py)
- **Description:** This script defines a function `no_c(my_string)` that removes all occurrences of characters 'c' and 'C' from a given string and returns the new string.

### 6. Print a matrix of integers
- **File:** [6-print_matrix_integer.py](./0x03-python-data_structures/6-print_matrix_integer.py)
- **Description:** This script defines a function `print_matrix_integer(matrix)` that prints a matrix of integers. The matrix is provided as a list of lists.

### 7. Add two tuples
- **File:** [7-add_tuple.py](./0x03-python-data_structures/7-add_tuple.py)
- **Description:** This script defines a function `add_tuple(tuple_a, tuple_b)` that adds corresponding elements of two tuples and returns a new tuple with the results.

### 8. Multiple returns
- **File:** [8-multiple_returns.py](./0x03-python-data_structures/8-multiple_returns.py)
- **Description:** This script defines a function `multiple_returns(sentence)` that returns a tuple containing the length of a string and its first character. If the string is empty, the first character is set to `None`.

### 9. Find the max integer in a list
- **File:** [9-max_integer.py](./0x03-python-data_structures/9-max_integer.py)
- **Description:** This script defines a function `max_integer(my_list)` that finds the largest integer in a given list. If the list is empty, it returns `None`.

### 10. Check if integers in a list are divisible by 2
- **File:** [10-divisible_by_2.py](./0x03-python-data_structures/10-divisible_by_2.py)
- **Description:** This script defines a function `divisible_by_2(my_list)` that creates a new list indicating whether each integer in the given list is divisible by 2.

### 11. Delete an element at a specific position in a list
- **File:** [11-delete_at.py](./0x03-python-data_structures/11-delete_at.py)
- **Description:** This script defines a function `delete_at(my_list, idx)` that deletes the item at a specific position in a list. If the index is negative or out of range, it returns the same list.

### 12. Switch values of two variables
- **File:** [12-switch.py](./0x03-python-data_structures/12-switch.py)
- **Description:** This script switches the values of two variables `a` and `b` and prints the result.

### 13. Check if a linked list is a palindrome
- **Files:** [13-is_palindrome.c](./0x03-python-data_structures/13-is_palindrome.c), [lists.h](./0x03-python-data_structures/lists.h)
- **Description:** This C program defines a function `is_palindrome` that checks if a singly linked list is a palindrome. An empty list is considered a palindrome.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your_username/alx-higher_level_programming.git
```

2. Navigate to the specific task directory:

```bash
cd alx-higher_level_programming/0x03-python-data_structures/
```

3. Run the Python script or compile and run the C program:

```bash
python3 0-print_list_integer.py
```

For C programs:

```bash
gcc -Wall -Werror -Wextra -pedantic 13-main.c linked_lists.c 13-is_palindrome.c -o palindrome
./palindrome
```