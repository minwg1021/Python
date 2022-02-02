#아파트의 k층 n호에 몇 명이 살고있는지
#계산하여 출력하는 프로그램

input_test_case = int(input())
input_case_list = []
input_case = []
result_list = []
for index in range(0,input_test_case):
    input_floor = int(input())
    input_home_number = int(input())
    input_case.append(input_floor)
    input_case.append(input_home_number)
    input_case_list.append(input_case)
    input_case = []

while input_case_list:
    input_case = input_case_list.pop(0)
    for room in range(0, input_case[1] + 1):
        result_list.append(room + 1)
    for floor in range(0, input_case[0]):
        for room in range(0, input_case[1]):
            result_list[room + 1] = result_list[room] + result_list[room + 1]
    print(result_list[input_case[1] - 1])
    result_list = []