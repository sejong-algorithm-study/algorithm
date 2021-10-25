from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check(Map, visited, n, m):
    global Max
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and Map[i][j] == 0:
                cnt += 1
    if Max < cnt:
        Max = cnt
def BFS(Map, n, m):
    visited = [[False]*m for _ in range(n)]
    global tmp
    queue = tmp
    queue = deque(queue)
    for i in queue:
        visited[i[0]][i[1]] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not visited[nx][ny] and Map[nx][ny] == 0:
                queue.append([nx, ny])
                visited[nx][ny] = True
    check(Map, visited, n, m)    


def printf(Map, n, m):
    print("start")
    for i in range(n):
        for j in range(m):
            print(Map[i][j], end=" ")
        print()
    print("-end-")
def recursive(Map, n, m, d, x, y):
    global cnt
    if d == 3:
        BFS(Map, n, m)
        return
    
    for i in range(x, n):
        for j in range(m):
            if Map[i][j] == 0:
                Map[i][j] = 1
                # printf(Map, n, m)
                recursive(Map, n, m, d + 1, i, j)
                Map[i][j] = 0

def findVirus(tmp, n, m):
    for i in range(n):
        for j in range(m):
            if Map[i][j] == 2:
               tmp.append([i, j]) 

n, m = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
tmp = []
Max = 0
findVirus(tmp, n, m)
recursive(Map, n, m, 0, 0, 0)

print(Max)
