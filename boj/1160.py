m, a, c, x0, n, g = map(int, input().split(" "))

d = dict()
d[1] = (a, 1)


def GetSomeNum(n):
    if n in d:
        return d[n]
    if n % 2 == 0:
        k = n // 2
        p, q = GetSomeNum(k)
        d[n] = ((p**2) % m, ((p + 1) * q) % m)
        return d[n]
    else:
        k = n // 2
        p, q = GetSomeNum(k)
        d[n] = ((a * (p**2)) % m, (p**2 + (p + 1) * q % m))
        return d[n]


p, q = GetSomeNum(n)
answer = ((p * x0 + c * q) % m) % g
print(answer)
