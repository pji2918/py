import math


def area_and_circumference(r):
    return math.pi * r**2, 2 * math.pi * r


while True:
    r = int(input("반지름을 입력하시오(-1이 입력되면 종료): "))
    if r == -1:
        break
    else:
        print(str.format("넓이 : {0:.3f}, 둘레 : {1:.3f}", *area_and_circumference(r)))
print("프로그램을 종료합니다.")
