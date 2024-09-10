n = int(input())

c = list(map(int, input().split()))

ymoney = 0
mmoney = 0

for i in c:
    ymoney += ((i // 30) + 1) * 10
    mmoney += ((i // 60) + 1) * 15

if ymoney < mmoney:
    print(str.format("Y {}", ymoney))
elif mmoney < ymoney:
    print(str.format("M {}", mmoney))
else:
    print(str.format("Y M {}", ymoney))
