#!/usr/bin/python3
def uppercase(str):
    for x in str:
        tmp = x
        if ord(tmp) >= 97 and ord(tmp) <= 122:
            tmp = chr(ord(x) - 32)
            print("{}".format(tmp), end='')
    print()
