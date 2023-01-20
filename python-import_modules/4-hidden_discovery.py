#!/usr/bin/python3
if __name__ == "__main__":
    import sys, hidden_4

    names = dir(hidden_4)

    for name in names:
        if name[0:2] == "__":
            pass
        else:
            print("{}".format(name))
