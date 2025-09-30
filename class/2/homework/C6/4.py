def max_and_min(n1, n2, n3):
    return max(n1, n2, n3), min(n1, n2, n3)


n1, n2, n3 = map(int, input("3 수를 입력하시오 : ").split())
print(str.format("가장 큰 수 : {0}\n가장 작은 수 : {1}", *max_and_min(n1, n2, n3)))
