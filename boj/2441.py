rep = int(input())

for i in range(rep, 0, -1):
    for j in range(0, rep - i, 1):
        print(" ", end="")
    for j in range(0, i, 1):
        print("*", end="")
    print()
