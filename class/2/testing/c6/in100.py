for i in range(2):
    integerNumber = int(input("정수를 입력하세요 : "))
    print(
        f"입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요? {integerNumber % 2 == 0 and integerNumber >= 0 and integerNumber <= 100}"
    )
