#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    size = len(sys.argv) - 1
    if size == 0:
        print("0 arguments.")
    
    elif size == 1:
        print("{} argument:".format(size))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(size))
        for x in range(size):
            print("{}: {}".format(x + 1, sys.argv[x + 1]))


