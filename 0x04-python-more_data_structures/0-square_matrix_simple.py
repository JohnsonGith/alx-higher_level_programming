#!/usr/bin/python3

def squre_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    return[[x **2 for x in row] for row in matrix]
