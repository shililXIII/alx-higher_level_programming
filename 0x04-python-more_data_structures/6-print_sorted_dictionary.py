#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_list = list(a_dictionary.keys())
    my_list.sort()
    for x in my_list:
        print("{}: {}".format(x, a_dictionary.get(x)))
