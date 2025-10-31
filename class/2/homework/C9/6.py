import re

s = input("문장 s : ")
s = re.sub(r"\D", " ", s)

score = []
for i in s.split():
    if i.isdigit():
        score.append(int(i))


print(f"총점 : {sum(score)}")
print(f"평균점수   {sum(score) / len(score)}")
