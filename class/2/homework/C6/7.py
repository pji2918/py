def factorial(n):
    sum = 1
    for i in range(1, n + 1):
        sum *= i
    return sum


print(f"{factorial(5)}")
print(f"{factorial(7)}")
print(f"{factorial(10)}")
