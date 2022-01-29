#순서대로 나열된 분수들 중 
#X번째 분수를 구하는 프로그램

input_number = input()
number = 1
temporary_number = 0
temporary_number_list = []

while number < int(input_number):
    input_number = int(input_number) - number
    number += 1
temporary_number = number
if number % 2 != 0:
    for value in range(1, number+1):
        temporary_number_list.append(str(temporary_number) + "/" + str(value))
        temporary_number -= 1
else:
    for value in range(1, number+1):
        temporary_number_list.append(str(value) + "/" + str(temporary_number))
        temporary_number -= 1

print(temporary_number_list[int(input_number)-1])
