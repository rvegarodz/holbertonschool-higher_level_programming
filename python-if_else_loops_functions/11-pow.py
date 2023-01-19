#!/usr/bin/python3
def pow(a, b):
    base = a
    if b == 0:
        return 1
    elif b > 0:
        for i in range(1, b):
            base *= a
        return base
    elif b < 0:
        b *= -1
        for i in range(1, b):
            base *= a
        result = 1/base
        return result

print(pow(100, -2))