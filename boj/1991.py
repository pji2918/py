import sys as s

n = int(s.stdin.readline().strip())
t = {}

for _ in range(n):
    r, l, ri = s.stdin.readline().strip().split()
    t[r] = [l, ri]


def p(r):
    if r != ".":
        print(r, end="")  # root
        p(t[r][0])  # left
        p(t[r][1])  # right


def i(r):
    if r != ".":
        i(t[r][0])  # left
        print(r, end="")  # root
        i(t[r][1])  # right


def po(r):
    if r != ".":
        po(t[r][0])  # left
        po(t[r][1])  # right
        print(r, end="")  # root


p("A")
print()
i("A")
print()
po("A")
