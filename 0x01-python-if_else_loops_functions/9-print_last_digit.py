#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        l_num = (-number % 10)
    elif number >= 0:
        l_num = number % 10
        print("{:d}".format(l_num), end="")
        return l_num
