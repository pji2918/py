n, m = map(int, input().split())
arrs = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]

for i in range(2):
    for j in range(n):
        arrs[i][j] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        print(arrs[0][i][j] + arrs[1][i][j], end=" ")
    print()
