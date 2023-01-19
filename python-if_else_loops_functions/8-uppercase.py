#!/usr/bin/python3
def uppercase(str):
    for i in str:
        num = ord(i)
        if num >= 97 and num <= 122:
            num -= 32
            letter = chr(num)
        else:
            letter = chr(num)
        print("{}".format(letter), end="")
    print("")
