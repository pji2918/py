import sys

input = sys.stdin.readline

rep = int(input())

ls = []

for i in range(rep):
    ls.append(list(map(int, input().split())))

x_count = {}
y_count = {}
for x, y in ls:
    x_count[x] = x_count.get(x, 0) + 1
    y_count[y] = y_count.get(y, 0) + 1

result = 0
for x, y in ls:
    result += (x_count[x] - 1) * (y_count[y] - 1)

print(result)
