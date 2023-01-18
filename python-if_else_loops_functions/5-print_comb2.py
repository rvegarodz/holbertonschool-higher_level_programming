#!/usr/bin/python3
for value in range (00, 100):
    if value < 99:
        if value < 10:
            base = 0
        else:
            base = ""
        print(f"{base}{value}, ", end="")
    else:
        print(f"{value}")