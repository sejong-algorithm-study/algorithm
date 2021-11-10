from collections import deque
import sys

input = sys.stdin.readline

x1 = [1, -1, 0, 0]
y1 = [0, 0, 1, -1]
x2 = [1, 1, -1, -1, 2, 2, -2, -2]
y2 = [2, -2, 2, -2, 1, -1, 1, -1]

def bfs():
    q.append([0, 0, 0]) #x,y,이동횟수
    c[0][0][0] = 1
    #큐에 남아있으면
    while q:
        x, y, z = q.popleft()
        if x == h-1 and y == w-1:
            print(c[x][y][z]-1)
            return
        if z < k:
            horse(x, y, z)
            monkey(x, y, z)
        elif z == k:
            monkey(x, y, z)

    print(-1)

def horse(x, y, z):
    for i in range(8):
        nx = x + x2[i]
        ny = y + y2[i]
        if 0 <= nx and nx < h and 0 <= ny and ny < w:
            if a[nx][ny] == 0 and c[nx][ny][z+1] == 0:
                c[nx][ny][z+1] = c[x][y][z] + 1
                q.append([nx, ny, z+1])

def monkey(x, y, z):
    for i in range(4):
        nx = x + x1[i]
        ny = y + y1[i]
        if 0 <= nx and nx < h and 0 <= ny and ny < w:
            if a[nx][ny] == 0 and c[nx][ny][z] == 0:
                c[nx][ny][z] = c[x][y][z] + 1
                q.append([nx, ny, z])

k = int(input())
w, h = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]
c = [[[0]*(k+1) for i in range(w)] for j in range(h)]
q = deque()

bfs()