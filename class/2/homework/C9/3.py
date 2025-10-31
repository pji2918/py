txt = input("문자열을 입력하시오 : ")

upperCnt = 0
lowerCnt = 0
numberCnt = 0
specialCnt = 0

for i in txt:
    if i.isupper():
        upperCnt += 1
    elif i.islower():
        lowerCnt += 1
    elif i.isdigit():
        numberCnt += 1
    else:
        specialCnt += 1

print("대문자, 소문자, 숫자, 특수문자의 수")
print(f"대문자 = {upperCnt}")
print(f"소문자 = {lowerCnt}")
print(f"숫자 = {numberCnt}")
print(f"특수문자 = {specialCnt}")
