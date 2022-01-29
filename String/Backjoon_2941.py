#입력 받은 크로아티아 알파벳이 몇 개의 단어인지
#구분해서 출력하는 프로그램
# c=, c-, dz=, d-, lj, nj, s=, z=

input_string = input()
poped_alphabet = ""
common_alphabet =""
count = 0

for alphabet in list(input_string):    
    poped_alphabet = poped_alphabet + alphabet
    if 'dz=' in poped_alphabet:
        count += 1
        poped_alphabet = poped_alphabet[:-3]
        if poped_alphabet:
            common_alphabet = common_alphabet + poped_alphabet
            poped_alphabet = ""
    elif ('c=' in poped_alphabet or 'c-' in poped_alphabet 
        or 'd-' in poped_alphabet or 'lj' in poped_alphabet 
        or 'nj' in poped_alphabet or 's=' in poped_alphabet 
        or 'z=' in poped_alphabet):
            count += 1
            poped_alphabet = poped_alphabet[:-2]
            if poped_alphabet:
                common_alphabet = common_alphabet + poped_alphabet
                poped_alphabet = ""
while poped_alphabet:
    count += 1
    poped_alphabet = poped_alphabet[:-1]
while common_alphabet:
    count += 1
    common_alphabet = common_alphabet[:-1]
print(count)
