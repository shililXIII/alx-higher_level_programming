#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) >= ord('a') and ord(x) <= ord('z'):
            x= chr(ord(x) - 32)
            print("{}".format(x), end= "")
    print()
