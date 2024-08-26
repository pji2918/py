abc = list(map(int, input().split(" ")))
s = input()

abc.sort()

for i in range(3):
    if s[i] == "A":
        print(abc[0], end=" ")
    elif s[i] == "B":
        print(abc[1], end=" ")
    elif s[i] == "C":
        print(abc[2], end=" ")
