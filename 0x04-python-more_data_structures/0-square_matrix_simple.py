#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in matrix:
        new_matrix.append([c**2 for c in x])
        return new_matrix
