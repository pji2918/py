while True:
    width = 1
    n = input().strip()

    if n == "0":
        break
    else:
        for i in n:
            if i == "1":
                width += 2
            elif i == "0":
                width += 4
            else:
                width += 3
            width += 1

    print(width)
