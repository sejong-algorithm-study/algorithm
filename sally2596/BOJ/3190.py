import sys
from collections import deque
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
arr = [[0] * n for _ in range(n)]
for i in range(k):
    x, y = map(int, sys.stdin.readline().split())
    arr[x - 1][y - 1] = 1

l = int(sys.stdin.readline())
snake = []
for i in range(l):
    x, c = sys.stdin.readline().split()
    snake.append([int(x), c])

arr[0][0] = -1  # 현재 뱀 위치

direction = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

m = 0
cnt = 0
headx = heady = 0
body =deque([[0,0]])

while True:
    if m < l and cnt == snake[m][0]:
        if snake[m][1] == 'D':
            direction = (direction + 1) % 4
        elif snake[m][1] == 'L':
            direction = (direction - 1) % 4
        m += 1

    nextheadx = headx + dx[direction]
    nextheady = heady + dy[direction]

    if nextheadx<0 or nextheadx>=n or nextheady<0 or nextheady>=n:
        cnt+=1
        break
    elif arr[nextheadx][nextheady]==-1:
        cnt+=1
        break
    elif arr[nextheadx][nextheady]==1:
        headx = nextheadx
        heady = nextheady
        body.append([headx, heady])
        arr[headx][heady] = -1
        cnt += 1
    else:
        [x,y] = body.popleft()
        arr[x][y] = 0
        headx = nextheadx
        heady = nextheady
        body.append([headx,heady])
        arr[headx][heady] = -1
        cnt += 1
print(cnt)
