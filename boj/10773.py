import sys

input = sys.stdin.readline()

k = int(input())
lst = []

for i in range(k):
    n = int(input())
    # 입력이 0인 경우 가장 최근에 쓴 수를 지우고
    # 0이 아닐 경우 해당 수를 쓴다
    lst.append(n) if n else lst.pop()

print(sum(lst))
