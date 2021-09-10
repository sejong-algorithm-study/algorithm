import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for __ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = r, c
result, cnt = 0, 0

while True:
    # 1
    if graph[x][y] == 0:
        result += 1
        graph[x][y] = 2

    # setting
    i = (d + 3) % 4
    nx, ny = x + dx[i], y + dy[i]
    
    back_idx = (d + 2) % 4
    bnx, bny = x + dx[back_idx], y + dy[back_idx]

    # 2-a
    if not graph[nx][ny]:
        x, y, d = nx, ny, i
        cnt = 0
    # 2-b
    elif cnt < 4:
        d = i
        cnt += 1
    # 2-d
    elif graph[bnx][bny] == 1:
        break
    # 2-c
    else:
        x, y = bnx, bny
        cnt = 0

print(result)