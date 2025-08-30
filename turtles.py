import turtle

t = turtle.Turtle()
t.shape("turtle")

# for i in range(3, 11):
#     sides = i

#     for _ in range(sides):
#         t.forward(100)
#         t.left(360 / sides)

t.pensize(3)

t.forward(100)
t.right(135)
t.forward(100)
t.penup()
t.right(180)
t.forward(50)
t.pendown()
t.right(90)
t.forward(50)

t.penup()
t.home()
t.forward(130)
t.right(90)
t.pendown()
t.forward(100)

t.penup()
t.home()
t.forward(30)
t.penup()
t.right(90)
t.forward(130)
t.pendown()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.penup()
t.right(180)
t.forward(100)
t.left(90)
t.pendown()
t.forward(50)

t.hideturtle()
turtle.done()
