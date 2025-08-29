import turtle

t = turtle.Turtle()
t.shape("turtle")

for i in range(3, 11):
    sides = i

    for _ in range(sides):
        t.forward(100)
        t.left(360 / sides)

turtle.done()