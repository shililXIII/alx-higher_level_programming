#!/usr/bin/python3
def uniq_add(my_list = []):
    uniq_add = set(my_list)
    number = 0
    for x in uniq_add:
        number += x
        return (number)
