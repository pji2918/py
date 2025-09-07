import turtle

t = turtle.Turtle()

t.speed(10)

for i in range(30, 600, 30):
    t.forward(i)
    t.left(90)

turtle.done()
