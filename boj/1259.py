while True:
    a = int(input())
    if a != 0:
        if str(a) == str(a)[::-1]:
            print("yes")
        else:
            print("no")
    else:
        break
