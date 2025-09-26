import turtle

sides = int(turtle.textinput("", "몇각형을 원하시나요?:"))  # type: ignore

t = turtle.Turtle()
t.speed(10)

for i in range(sides):
    t.forward(100)
    t.left(360 / sides)

turtle.done()
