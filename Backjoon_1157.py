#알파벳 대소문자 구분X / 단어에서 가장 많이 사용된
#알파벳이 무엇인지 알아내는 프로그램
import operator

alphabet_dictionary = {}
input_string = input()
divide_list = list(input_string.lower())
max = 0

for number in range(1, 27):
    alphabet_dictionary.update({chr(number + 96): 0})

for alphabet in divide_list:
    for key, value in alphabet_dictionary.items():
        if key == alphabet:
            value += 1
            alphabet_dictionary.update({key: value})

for key, value in sorted(alphabet_dictionary.items(), key=operator.itemgetter(1), reverse=True)[:2]:
    if max == 0:
        result_key = str(key).upper()
        max = value
        continue
    if max == value:
        print('?')
        break
    else:
        print(result_key)
        break
    

    

