#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2023 개정판)
# LAB 9-3 트위터 메시지 처리
#

s = "It's Not The Right Time To Conduct Exams. MY DEMAND IN BOLD AND CAPITAL. NO EXAMS IN COVID!!!"

print(f"입력={s}")
count = 0
for word in s.split():
    if word == word.upper():  # 대문자로 변환한 것과 동일하면 대문자 단어
        count += 1

upperCnt = 0
puncCnt = s.count("!")
for chr in s:
    if chr.isupper():
        upperCnt += 1

upperCnt2 = sum(chr.isupper() for chr in s)

print(f"\n대문자 단어의 수={count}")
print(f"느낌표 갯수={puncCnt}")
print(f"대문자 갯수={upperCnt2}")
t = s.lower()
t = t.replace("!", "")
t = t.replace(".", "")
t = t.replace("'", "")
print(f"결과={t}")
