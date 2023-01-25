#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def pow(lyst=[]):
        lyst_copy = []
        for value in lyst:
            lyst_copy.append(value * value)
        return lyst_copy
    
    new_matrix = list(map(pow, matrix))
    return new_matrix
