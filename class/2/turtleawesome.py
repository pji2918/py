import turtle

# turtle.setup(400, 400)
# turtle.bgcolor("black")

t = turtle.Turtle(shape="turtle")
t.penup()

x = int(turtle.textinput("숫자 입력", "숫자 x를 입력하십시오."))  # type: ignore
x = int(turtle.textinput("숫자 입력", "숫자 y를 입력하십시오."))  # type: ignore

t.goto(100, 100)
t.write("두 수 모두 양수.")
t.goto(-100, 100)
t.write("두 번째 수만 음수.")
t.goto(-100, -100)
t.write("두 수 모두 음수.")
t.goto(100, -100)
t.write("두 수 모드 음수.")

# if pos > 0:
#     t.goto(100, 100)
# elif pos < 0:
#     t.goto(100, -100)
# else:
#     t.goto(100, 0)

# t.speed(0)
# t.pencolor("orange")

# for i in range(200):
#     t.forward(i)
#     t.left(93)

turtle.done()
