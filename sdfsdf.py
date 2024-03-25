N = int(input())
target = int(input())
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
if N % 2 == 1:
    x, y = N // 2, N // 2
else:
    x, y = N // 2, N // 2 - 1

m = [[0] * N for _ in range(N)]
m[x][y] = 1
cnt = 2
dir = 0
num = 2
while True:
    for _ in range(cnt - 1):
        nx, ny = x + dx[dir], y + dy[dir]
        m[nx][ny] = num
        num += 1

        if num == N**2 + 1:
            break
        x, y = nx, ny

    if num == N**2 + 1:
        break

    dir = (dir + 1) % 4
    # 위나 아래로 갈때 숫자 1 증가
    if dir == 0 or dir == 2:
        cnt += 1

for i in m:
    print(*i)
for i in range(N):
    for j in range(N):
        if m[i][j] == target:
            print(i + 1, j + 1)
