from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move_marble(x, y, dx, dy):
    while True:
        x += dx
        y += dy

        if board[x][y] == '#':
            x -= dx
            y -= dy
            return x, y

        if board[x][y] == 'O':
            return x, y


def bfs(red_x, red_y, blue_x, blue_y):
    q = deque([[red_x, red_y, blue_x, blue_y]])
    visited = [(red_x, red_y, blue_x, blue_y)]
    cnt = 0

    while q:
        for _ in range(len(q)):
            red_x, red_y, blue_x, blue_y = q.popleft()
            if cnt > 10:
                return -1
            if board[red_x][red_y] == 'O':
                return cnt

            for i in range(4):
                red_x2, red_y2 = move_marble(red_x, red_y, dx[i], dy[i])
                blue_x2, blue_y2 = move_marble(blue_x, blue_y, dx[i], dy[i])

                if board[blue_x2][blue_y2] == 'O':
                    continue

                if red_x2 == blue_x2 and red_y2 == blue_y2:
                    move_red = abs(red_x2 - red_x) + abs(red_y2 - red_y)
                    move_blue = abs(blue_x2 - blue_x) + abs(blue_y2 - blue_y)
                    if move_red < move_blue:
                        blue_x2 -= dx[i]
                        blue_y2 -= dy[i]
                    else:
                        red_x2 -= dx[i]
                        red_y2 -= dy[i]

                if (red_x2, red_y2, blue_x2, blue_y2) not in visited:  # 방문해본적이 없는 위치라면 새로 큐에 추가 후 방문 처리
                    q.append([red_x2, red_y2, blue_x2, blue_y2])
                    visited.append((red_x2, red_y2, blue_x2, blue_y2))
        cnt += 1
    return -1


n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(input()))
    for j in range(m):
        if board[i][j] == 'R':
            x1, y1 = i, j
        elif board[i][j] == 'B':
            x2, y2 = i, j

print(bfs(x1, y1, x2, y2))
