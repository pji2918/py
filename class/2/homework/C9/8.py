import re

txt = input("문장을 입력하시오 : ")
txt = re.sub(r"[^\s\w]", "", txt)

alphas = []
numbers = []
mixed = []
for i in txt.split():
    if i.isalpha():
        alphas.append(i)
    elif i.isdigit():
        numbers.append(i)
    else:
        mixed.append(i)

print(f"영문 단어 : {' '.join(alphas)}")
print(f"숫자 : {' '.join(numbers)}")
print(f"영문자+숫자 : {' '.join(mixed)}")
