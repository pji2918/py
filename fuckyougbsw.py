length = int(input())

rang = 0

for i in range(length):
    rang = input().split(" ")
    txt = input()
    if float(rang[1]) % len(txt) == 0:
        print("yes")
    else:
        print("no")
