s: str = "test"


def f(q: str) -> str:
    return str.join(s, q)


print(f(s))
