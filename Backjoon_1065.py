input_number = input()
divide_number_list = []
poped_number = 0
compare_number_list = []
count = 0
value = 0
copy_value = 0
while value < int(input_number):
    value += 1
    copy_value = value
    if value < 100:
        count += 1
    else:
        while copy_value != 0:
            divide_number_list.append(int(copy_value % 10))
            copy_value = int(copy_value / 10)
        while len(divide_number_list) != 1:
            poped_number = divide_number_list.pop()
            compare_number_list.append(int(poped_number) - int(divide_number_list[-1]))
        divide_number_list.clear()
        if len(set(compare_number_list)) == 1:
            count += 1
        compare_number_list.clear()
print(count)
