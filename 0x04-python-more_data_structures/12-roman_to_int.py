#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    char = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [char[x] for x in roman_string] + [0]
    r_char = 0
    for y in range(len(numbers) - 1):
        if numbers[y] >= numbers[y + 1]:
            r_char += numbers[y]
        else:
            r_char -= numbers[y]
            return r_char
