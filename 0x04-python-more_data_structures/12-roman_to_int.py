#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)

    total = 0
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                  "D": 500, "M": 1000}

    for idx, current_symbol in enumerate(roman_string):
        current_value = roman_dict.get(current_symbol)

        if idx < len(roman_string) - 1:
            next_symbol = roman_string[idx + 1]
            next_value = roman_dict.get(next_symbol)

            if next_value > current_value:
                total -= current_value
            else:
                total += current_value
        else:
            total += current_value

    return (total)
