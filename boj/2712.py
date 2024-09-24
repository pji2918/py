t = int(input())

for i in range(t):
    n, u = input().split()
    n = float(n)

    if u == "kg":
        print(f"{n * 2.2046:.4f} lb")
    elif u == "l":
        print(f"{n * 0.2642:.4f} g")
    elif u == "lb":
        print(f"{n * 0.4536:.4f} kg")
    elif u == "g":
        print(f"{n * 3.7854:.4f} l")
