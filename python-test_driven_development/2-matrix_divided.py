#!/usr/bin/python3
""" COMMENT """


def matrix_divided(matrix, div):
    """ COMMENT """
    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "Each row of the matrix must have the same size"
    if type(matrix) != list:
        raise TypeError(msg1)
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(div) != int and type(div) != float:
        raise TypeError('div must be a number')
    og_len = len(matrix)
    if og_len > 1:
        for i in range(og_len):
            if len(matrix[0]) != len(matrix[1]):
                raise TypeError(msg2)
    for idx in range(og_len):
        for idx_l in range(len(matrix[idx])):
            if type(matrix[idx][idx_l]) != int:
                if type(matrix[idx][idx_l]) != float:
                    raise TypeError(msg1)
    def divide(og_matrix):
        """ COMMENT """
        matrix_copy = []
        for i in og_matrix:
            matrix_copy.append(round(i / div, 2))
        return matrix_copy
    return list(map(divide, matrix))
