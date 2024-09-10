import math

t = int(input())

for i in range(t):
    a, b = map(int, input().split(" "))
    print(str.format("{} {}", math.lcm(a, b), math.gcd(a, b)))
