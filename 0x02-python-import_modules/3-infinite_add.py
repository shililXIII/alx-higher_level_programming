#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    finish = 0
    if finish == 0:
        print("{}".format(finish))
    for x in range(len(sys.argv) - 1):
        finish += int(sys.argv[x + 1])
        print("{}".format(finish))
