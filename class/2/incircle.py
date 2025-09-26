from math import sqrt

x, y = map(int, input("점의 좌표 x, y를 입력하시오 : ").split())
x = abs(x - 3)
y = abs(y - 4)

if sqrt(x**2 + y**2) <= 10:
    print("원의 내부에 있음")
else:
    print("원의 외부에 있음")
