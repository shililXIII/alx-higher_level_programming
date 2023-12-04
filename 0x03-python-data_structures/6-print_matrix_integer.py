#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if y != len(matrix[x]) - 1:
                    z = ' '
                else:
                    z = '' 
                print("{:d}".format(matrix[x][y]), end=z)
                print()
