import math


def distance(x1, y1, x2, y2):
    if x1 == x2:
        return max(y1, y2) - min(y1, y2)
    elif y1 == y2:
        return max(x1, x2) - min(x1, x2)
    else:
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
print(f"({x1},{y1})과 ({x2},{y2}) 사이의 거리는 {distance(x1, y1, x2, y2)}")
