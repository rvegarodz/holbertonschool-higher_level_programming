#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None or (len(sentence) == 0):
        new_tuple = (len(sentence), None)
    else:
        new_tuple = (len(sentence), sentence[0])
    return new_tuple
