import turtle

sc = turtle.Screen()
sc.bgcolor("lightblue")
sc.title("Draw Triangle")

t = turtle.Turtle()
t.color("hotpink")
t.pensize(3)
t.speed(0)

t.penup()
t.goto(0, 250)
t.pendown()

t.begin_fill()
for i in range(3):
    t.forward(80)
    t.left(120)
t.end_fill()

t.penup()
t.right(180)
t.forward(80)

turtle.done()
