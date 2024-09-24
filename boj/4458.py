n = int(input())

l = []

for i in range(n):
    l.append(input())

for i in l:
    print(i[0].upper() + i[1:])
