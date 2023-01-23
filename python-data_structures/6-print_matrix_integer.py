#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print("")
    else:
        for row in matrix:
            len_row = len(row)
            count = 0
            for value in row:
                count = count + 1
                if count < len_row:
                    print("{:d}".format(value), end=" ")
                elif count == len_row:
                    print("{:d}".format(value), end="")
            print("")
