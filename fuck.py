import math
import statistics

n = int(input())

difficulty = list()

for i in range(n):
    difficulty.append(int(input()))

rate = round(len(difficulty) * 0.15)

difficulty.sort(reverse=True)


difficulty = [i for i in difficulty if i in difficulty[: (rate - 1)]]
difficulty = [i for i in difficulty if i in difficulty[-rate:]]

avg = round(statistics.mean(difficulty))

print(avg)
