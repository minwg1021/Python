#호텔에 들어온 손님들을 조건에 맞는 방에
#배정하는 프로그램

input_cases = int(input())
input_case = []
input_case_list = []
count = 1
floor_number = 0
room_number = 1
for value in range(0, input_cases):
    input_height, input_width, input_customer = input().split()
    input_case.append(int(input_height))
    input_case.append(int(input_width))
    input_case.append(int(input_customer))
    input_case_list.append(input_case)
    input_case = []

while input_case_list:
    input_case = input_case_list.pop(0)
    floor_number = input_case[0]
    input_case[0] = 0
    for count in range(0, input_case[-1]):
        if input_case[0] == floor_number:
            input_case[0] = 0
            room_number += 1
        input_case[0] += 1
    if room_number < 10:
        print(str(input_case[0]) + "0" + str(room_number))
    else:
        print(str(input_case[0]) + str(room_number))

    room_number = 1
    floor_number = 0

