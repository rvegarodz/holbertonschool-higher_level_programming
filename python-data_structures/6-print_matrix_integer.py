#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print("")
    else:
        for row in matrix:
            for value in row:
                print("{:d}".format(value), end="")
                print("", end=" ")
            print("")
