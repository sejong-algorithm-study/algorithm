from collections import deque
import copy

move = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def melt_ice(now_x, now_y):
    queue = deque([[now_x, now_y]])

    while queue:
        x, y = queue.popleft()
        sea = 0

        for move_x, move_y in move:
            new_x = move_x + x
            new_y = move_y + y

            if 0 <= new_x < N and 0 <= new_y < M and not visited[new_x][new_y]:
                if iceberg[new_x][new_y] == 0:
                    sea += -1
                else:
                    visited[new_x][new_y] = True
                    queue.append([new_x, new_y])

        new_state = iceberg[x][y] + sea
        next_iceberg[x][y] = 0 if new_state < 0 else new_state


N, M = map(int, input().split())
next_iceberg = [list(map(int, input().split())) for _ in range(N)]
year = 0

while True:
    piece = 0
    iceberg = copy.deepcopy(next_iceberg)
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] == 0:
                continue

            if not visited[i][j]:
                piece += 1
                visited[i][j] = True
                melt_ice(i, j)

    if piece > 1:
        print(year)
        break

    if piece == 0:
        print(0)
        break

    year += 1
