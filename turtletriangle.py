import turtle
import math

t = turtle.Turtle()
t.shape("turtle")

# 직각삼각형 그리기

t.forward(100)
t.left(180 - 45)

daegaklength = math.sqrt((100**2) + (100**2))
t.forward(daegaklength)

t.left(180 - 45)
t.forward(100)

# 끝

# 정삼각형 2개 그리기

t.setheading(0)
t.right(60)
t.forward(100)

for _ in range(2):
    t.right(120)
    t.forward(100)

for _ in range(2):
    t.left(120)
    t.forward(100)

# 끝

turtle.done()
