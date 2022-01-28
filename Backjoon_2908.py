#두 숫자가 주어졌을때 숫자를 뒤집고
#어느 숫자가 더 큰지 판단하는 프로그램

input_number1, input_number2 = input().split()
reverse_number_list1 = []
reverse_number_list2 = []
value = 0
result_number1 = 0
result_number2 = 0

while int(input_number1) != 0:
    reverse_number_list1.append(int(input_number1) % 10)
    input_number1 = int(input_number1) / 10
while int(input_number2) != 0:
    reverse_number_list2.append(int(input_number2) % 10)
    input_number2 = int(input_number2) / 10

while reverse_number_list1:
    result_number1 = result_number1 + reverse_number_list1.pop() * (10 ** value)
    value += 1
value = 0
while reverse_number_list2:
    result_number2 = result_number2 + reverse_number_list2.pop() * (10 ** value)
    value += 1

max_number = max(result_number1, result_number2)
print(max_number)

