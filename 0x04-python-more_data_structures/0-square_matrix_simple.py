#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix."""
    return [[element**2 for element in row] for row in matrix]
