#!/usr/bin/python3
for i in range(0, 10):
    for j in range (0, 10):
        if i != j and j != i:
            print("{}{}".format(i, j), end="")
            if i+j < 100:
                print(", ".format(i, j), end="")
            else:
                print("")
