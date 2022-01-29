#단어가 주어졌을때 다이얼 전화기를 이용해서
#단어에 해당하는 전화를 걸기 위해 걸리는 시간을
#계산하는 프로그램

# ABC -> 3초
# DEF -> 4초
# GHI -> 5초
# JKL -> 6초
# MNO -> 7초
# PQRS -> 8초
# TUV -> 9초
# WXYZ -> 10초

input_string = input()
result_second = 0

for value in list(input_string):
    if value == 'A' or value == 'B' or value == 'C':
        result_second += 3
    elif value == 'D' or value == 'E' or value == 'F':
        result_second += 4
    elif value == 'G' or value == 'H' or value == 'I':
        result_second += 5
    elif value == 'J' or value == 'K' or value == 'L':
        result_second += 6
    elif value == 'M' or value == 'N' or value == 'O':
        result_second += 7
    elif value == 'P' or value == 'Q' or value == 'R' or value == 'S':
        result_second += 8
    elif value == 'T' or value == 'U' or value == 'V':
        result_second += 9
    elif value == 'W' or value == 'X' or value == 'Y' or value == 'Z':
        result_second += 10

print(result_second)
