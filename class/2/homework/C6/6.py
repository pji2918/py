from math import floor, sqrt


def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, floor(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


for _ in range(4):
    num = int(input("소수 검사를 할 정수를 입력하시오: "))
    print(f"소수인가요? : {is_prime(num)}")
