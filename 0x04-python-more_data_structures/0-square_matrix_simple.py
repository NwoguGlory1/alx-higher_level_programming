#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x :list(map(lambda y: (y**2),x)), matrix)))
        return (new_matrix)
