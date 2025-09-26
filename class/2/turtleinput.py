import turtle

t = turtle.Turtle()

while True:
    shape = turtle.textinput("", "도형을 입력하시오:")

    if shape == "사각형":
        width = int(turtle.textinput("", "가로:"))  # type: ignore
        height = int(turtle.textinput("", "세로:"))  # type: ignore
        for _ in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)
    elif shape == "삼각형":
        length = int(turtle.textinput("", "변의 길이:"))  # type: ignore
        for _ in range(3):
            t.left(180 - 60)
            t.forward(length)
    elif shape == "원":
        radius = int(turtle.textinput("", "반지름:"))  # type: ignore
        t.circle(radius)
    elif shape == "exit":
        break

turtle.done()
