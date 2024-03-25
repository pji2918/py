# 알림: 아래 코드는 Python 3 환경에서 시간 초과가 발생합니다. PyPy3를 사용하여 제출하거나, 맨 밑에 표시된 코드를 사용하십시오.

"""
def DoRound(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)


n = int(input())

if n == 0:
    print(0)
else:
    difficulty = []

    for i in range(n):
        difficulty.append(int(input()))

    rate = DoRound(n * 0.15)

    difficulty.sort()

    avg = DoRound(sum(difficulty[rate : n - rate]) / (n - (rate * 2)))

    print(avg)
"""

# 알림: 위 코드는 Python 3 환경에서 시간 초과가 발생합니다. PyPy3를 사용하여 제출하거나, 아래 코드를 사용하십시오.

import sys


def DoRound(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)


n = int(sys.stdin.readline())

if n == 0:
    print(0)
else:
    difficulty = []

    for i in range(n):
        difficulty.append(int(sys.stdin.readline()))

    rate = DoRound(n * 0.15)

    difficulty.sort()

    avg = DoRound(sum(difficulty[rate : n - rate]) / (n - (rate * 2)))

    print(avg)
