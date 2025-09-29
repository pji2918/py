import turtle

t = turtle.Turtle()


def square(size):
    for _ in range(4):
        t.forward(size)
        t.left(90)


def circle(radius):
    t.circle(radius)


def triangle(width):
    for _ in range(3):
        t.forward(width)
        t.left(360 / 3)


while True:
    userInput = input("도형과 크기 입력: ")

    if userInput[0] == "q":
        break
    else:
        shape, size = userInput.split()
        size = int(size)

        if shape == "s":
            square(size)
        elif shape == "c":
            circle(size)
        elif shape == "t":
            triangle(size)
