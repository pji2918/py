import random

numbers = list(range(1, 46))
random.shuffle(numbers)

# lotto = numbers[:6]
# lotto.sort()
# print(lotto)

print(f"{sorted(numbers[:6])}")
