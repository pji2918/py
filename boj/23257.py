# BOJ : 23257
# 결과 : 맞았습니다!!
# 작성자 : 손지호
# 난이도 : 골드 3

n, m = map(int, input().split())
a = list(map(int, input().split()))

mo = list()

for i in a:
    mo.append(abs(i))

month = set(mo)

for i in range(m - 1):
    month = set(i ^ j for i in month for j in mo)

print(max(month))
