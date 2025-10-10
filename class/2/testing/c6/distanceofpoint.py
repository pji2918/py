x1 = int(input("x1 좌표를 입력하시오 : "))
y1 = int(input("y1 좌표를 입력하시오 : "))
x2 = int(input("x2 좌표를 입력하시오 : "))
y2 = int(input("y2 좌표를 입력하시오 : "))

if x1 == x2:
    print(f"두 점의 거리: {max(x1, x2) - min(x1, x2)}")
elif y1 == y2:
    print(f"두 점의 거리: {max(y1, y2) - min(y1, y2)}")
else:
    widthSquare = (max(x1, x2) - min(x1, x2)) ** 2
    heightSquare = (max(y1, y2) - min(y1, y2)) ** 2
    print(f"두 점의 거리: {(widthSquare + heightSquare) ** 0.5}")
