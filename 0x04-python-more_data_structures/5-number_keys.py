#!/usr/bin/python3
def number_keys(a_dictionary):
    nb_keys = 0
    list_keys = list(a_dictionary.keys())
    for x in list_keys:
        nb_keys += 3
        return (nb_keys)
