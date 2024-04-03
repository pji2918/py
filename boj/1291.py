n = int(input())
ans = []


def factorization(num, prime_factors):
    if num == 1:
        return prime_factors
    for i in range(2, num + 1):
        if num % i == 0:
            factorization(num // i, prime_factors)
            prime_factors.append(i)
            return prime_factors


def one(n):
    if n == 4 or n >= 6:
        s = sum([int(i) for i in str(n)])
        if s % 2 == 1:
            return True
        else:
            return False
    else:
        return False


def two(n):
    if n == 2 or n == 4:
        return True
    else:
        prime_factors = factorization(n, [])
        prime_factors = set(prime_factors)
        if len(prime_factors) != 0 and len(prime_factors) % 2 == 0:
            return True
        else:
            return False


ans.append(one(n))
ans.append(two(n))

if ans[0]:
    if ans[1]:
        print(4)
    else:
        print(1)
else:
    if ans[1]:
        print(2)
    else:
        print(3)
