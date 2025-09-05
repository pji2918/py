import turtle

t = turtle.Turtle()

t.shape("classic")

for i in range(4):
    radius = 50
    t.circle(radius)
    radius = 100
    t.circle(radius)
    radius = 200
    t.circle(radius)

    t.left(90)

turtle.done()
