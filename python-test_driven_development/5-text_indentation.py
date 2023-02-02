#!/usr/bin/python3
"""COMMENT"""


def text_indentation(text):
    """COMMENT"""
    if type(text) != str:
        raise TypeError('text must be a string')
    else:
        char_cases = ['.', '?', ':']
        for idx in range(len(text)):
            if text[idx] in char_cases:
                print(text[idx])
                print()
            elif text[idx] == ' ' and text[idx - 1] in char_cases:
                continue
            else:
                print(text[idx], end='')
            