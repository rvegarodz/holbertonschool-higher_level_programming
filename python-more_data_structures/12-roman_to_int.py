#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dictionary = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000,}
    if roman_string:
        str_len = len(roman_string)
    if str_len == 1:
        return roman_dictionary.get(roman_string)
    else:
        namor = reversed(roman_string)
        namor_list = []
        for letter in namor:
            namor_list.append(roman_dictionary.get(letter))
        old_num = 0
        total_sum = 0
        for i in namor_list:
            if i < old_num:
                total_sum -= i
            else:
                total_sum += i
            old_num = i
        
    return total_sum