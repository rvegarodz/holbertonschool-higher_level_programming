#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    names = dir(hidden_4)

    for name in names:
        if name[3] == "__":
            continue
        else:
            print("{}".format(name))
