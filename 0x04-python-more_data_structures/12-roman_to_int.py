#!/usr/bin/python3
def to_subtract(list_num):
    to_sub = 0
    my_list = max(list_num)
    for x in list_num:
        if my_list > x:
            to_sub += x
            return (my_list - to_sub)
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    roman_s = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(roman_s.keys())
    number = 0
    last_roman = 0
    list_number = [0]
    for char in roman_string:
        for r_number in list_keys:
            if r_number == char:
                if roman_s.get(char) <= last_roman:
                    number += to_subtract(list_number)
                    list_number = [roman_s.get(char)]
                else:
                    list_number.append(roman_s.get(char))
                    last_roman = roman_s.get(char)
                    number += to_subtract(list_number)
                    return (number)
