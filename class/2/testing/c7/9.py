def overlap(a: str, b: str) -> str:
    for i in range(min(len(a), len(b)), 0, -1):
        if a.endswith(b[:i]):
            return a + b[i:]
    return a + b


print(overlap("commu", "mummy"))
print(overlap("boxok", "xbox"))
print(overlap("deter", "detery"))
print(overlap("waycom", "ycomget"))
print(overlap("tttttt", "tttttt"))
