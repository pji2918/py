string = input("문자열을 입력하세요 : ")

for i in range(len(string)):
    print(string[: i + 1])
for i in range(len(string) - 2, -1, -1):
    print(string[: i + 1])
