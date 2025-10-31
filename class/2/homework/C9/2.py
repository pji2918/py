lower = ""
upper = ""
txt = input("문자열을 입력하시오 : ")

for i in txt:
    if i.isupper():
        upper += i
    else:
        lower += i

print(f"{lower}{upper}")
