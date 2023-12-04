#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for emy in my_string:
        if emy != "c" and emy != "C":
            new_str += emy
    return new_str
