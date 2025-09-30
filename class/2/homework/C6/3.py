def max3(n1, n2, n3):
    return max(n1, n2, n3)


def min3(n1, n2, n3):
    return min(n1, n2, n3)


n1, n2, n3 = map(int, input("3 수를 입력하시오 : ").split())
print(f"가장 큰 수 : {max3(n1, n2, n3)}")
print(f"가장 작은 수 : {min3(n1, n2, n3)}")
