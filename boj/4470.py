n = int(input())

s = list()

for i in range(n):
    s.append(input())

for i in range(len(s)):
    print(str.format("{}. {}", i + 1, s[i]))
