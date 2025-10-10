x1 = int(input("x1 좌표를 입력하시오 : "))
y1 = int(input("y1 좌표를 입력하시오 : "))
x2 = int(input("x2 좌표를 입력하시오 : "))
y2 = int(input("y2 좌표를 입력하시오 : "))

width = max(x1, x2) - min(x1, x2)
height = max(y1, y2) - min(y1, y2)

print(f"직각삼각형의 면적은 : {(width * height) / 2}")
