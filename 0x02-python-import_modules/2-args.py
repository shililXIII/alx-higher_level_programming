#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    size = len(sys.argv) - 1
    if size == 0:
        print("0 arguments.")
    
    elif size == 1:
        print("{:d} argument:".format(size))
        print("{:d}: {}".format(1, sys.argv[1]))
    else:
        print("{:d} arguments:".format(size))
        for x in range(size):
            print("{:d}: {}".format(x + 1, sys.argv[x + 1]))


