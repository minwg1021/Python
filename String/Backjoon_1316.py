#단어 N개를 입력 받아 그룹 단어의 개수를
#출력하는 프로그램

input_number = int(input())
input_string = []
for value in range(0, input_number):
    input_string.append(input())
alphabet_dictionary = {}
count = 0
index = 0

for string in input_string:
    count += 1
    for alphabet in string:
        if alphabet not in alphabet_dictionary.keys():
            alphabet_dictionary.update({alphabet : 0})
        elif alphabet != string[index-1]:
            count -= 1
            break
        index += 1
    alphabet_dictionary = {}
    index = 0
print(count)
