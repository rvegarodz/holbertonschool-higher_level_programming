#!/usr/bin/python3
def pow(a, b):
    if (a <= 0 or a >= 0) and (b >= 0):
        for i in range(b):
            result = a * a
        return result
    elif (a <= 0 or a >= 0) and (b < 0):
        for i in range(b):
            result = a * a
            positive_result = 1/result
        return positive_result
