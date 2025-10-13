n = int(input("n을 입력하시오 : "))
numArray = list(range(1, n * n + 1))

for i in range(1, n + 1):
    if i % 2 != 0:
        tempArr = numArray[(n * i) - n : n * i]
        for ii in tempArr:
            print(f"{ii:2d}", end=" ")
    else:
        tempArr = numArray[n * i - 1 : (n * i) - n - 1 : -1]
        for ii in tempArr:
            print(f"{ii:2d}", end=" ")
    print()
