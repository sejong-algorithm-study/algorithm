import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]

for i in range(1, n - 1):
    for j in range(1, m - 1):
        if board[i][j] == 'R':
            red_i = i
            red_j = j
        elif board[i][j] == 'B':
            blue_i = i
            blue_j = j
        elif board[i][j] == 'O':
            hole_i = i
            hole_j = j

que = deque([[red_i, red_j, blue_i, blue_j, 0]])
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def move(now_i, now_j, dir_i, dir_j):
    cnt = 0
    while board[now_i + dir_i][now_j + dir_j] != "#" and board[now_i][now_j] != "O":
        now_i += dir_i
        now_j += dir_j
        cnt += 1

    return now_i, now_j, cnt

fin = 0
while (que):
    ri, rj, bi, bj, cnt = que.popleft()
    if fin == 1:
        break
    if cnt + 1 > 10:
        print(-1)
        break
    for k in range(4):
        nextri, nextrj, rcnt = move(ri, rj, dx[k], dy[k])
        nextbi, nextbj, bcnt = move(bi, bj, dx[k], dy[k])
        if board[nextbi][nextbj] != "O":
            if board[nextri][nextrj] == "O":
                print(cnt + 1)
                fin = 1
                break
            if nextrj == nextbj and nextbi == nextri:
                if rcnt > bcnt:
                    nextri -= dx[k]
                    nextrj -= dy[k]
                if rcnt < bcnt:
                    nextbi -= dx[k]
                    nextbj -= dy[k]
            que.append([nextri, nextrj, nextbi, nextbj, cnt + 1])
