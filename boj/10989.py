n = int(input())

c = [0] * 10001

for _ in range(n):
    num = int(input())
    c[num] += 1

for i in range(1, 10001):
    if c[i] != 0:
        for _ in range(c[i]):
            print(i)
