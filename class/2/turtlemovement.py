import random
import turtle

t = turtle.Turtle(shape="turtle")
t.width(3)
t.shapesize(3, 3)

for i in range(30):
    if random.randrange(2) == 0:
        t.right(90)
    else:
        t.left(90)
    t.forward(50)


# while True:
#     cmd = input("명령을 입력하시오: ")
#     if cmd.isdigit():
#         if int(cmd) <= 9 and int(cmd) >= 1:
#             t.shapesize(int(cmd))
#         else:
#             print(
#                 f"{cmd}은/는 허용되는 값이 아닙니다. 허용되는 값은 1-9 사이의 정수여야 합니다."
#             )
#     elif cmd == "l":
#         t.left(90)
#         t.forward(100)
#     elif cmd == "r":
#         t.right(90)
#         t.forward(100)
#     elif cmd == "f":
#         t.forward(100)
#     elif cmd == "h":
#         t.shapesize(10, 10)
#     elif cmd == "n":
#         t.shapesize(3, 3)
#     else:
#         print(f'"{cmd}"은/는 올바른 명령이 아닙니다.')

turtle.done()
