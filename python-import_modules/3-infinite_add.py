#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    value = 0
    lenght = len(sys.argv)
    for i in range(1, lenght):
        value += int(sys.argv[i])
    print("{}".format(value))
