i = 0
try:
    while input():
        i += 1
except EOFError:
    print(i)
