import math

primeNumbers = []
for i in range(2, 101):
    isPrime = True
    for ii in range(2, math.floor(math.sqrt(i)) + 1):
        if i % ii == 0:
            isPrime = False
    if isPrime:
        primeNumbers.append(i)

print("2에서 100사이의 소수들 : ")
print(primeNumbers)
