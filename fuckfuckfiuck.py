import sys

n = int(sys.stdin.readline())
words = [(sys.stdin.readline()).rstrip() for _ in range(n)]

words.sort(key=len)
cnt = 0

for i in range(n):
    flag = False
    for j in range(i + 1, n):
        if words[j].startswith(words[i]):
            flag = True
            break
    if not flag:
        cnt += 1

print(cnt)
