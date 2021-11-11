import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

hx = [1, 2, 2, 1, -1, -2, -2, -1]
hy = [2, 1, -1, -2, -2, -1, 1, 2]

k = int(sys.stdin.readline())
w, h = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
visited = [[[0 for i in range(w)] for j in range(h)] for l in range(31)]
mincnt= w*h+1

que = deque([[0, 0, 0, 0]])
flg=False
while que:
    x, y, cnt, myk = que.popleft()
    if x==h-1 and y==w-1:
        mincnt = min(cnt,mincnt)
        flg = True
        break
    if myk<k:
        for i in range(8):
            newx = x+hx[i]
            newy = y+hy[i]
            if 0<=newx<h and 0<=newy<w and arr[newx][newy]!=1 and visited[myk+1][newx][newy]==0:
                visited[myk+1][newx][newy]=1
                que.append([newx,newy,cnt+1,myk+1])
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if 0 <= newx < h and 0 <= newy < w and arr[newx][newy] != 1 and visited[myk][newx][newy]==0:
            visited[myk][newx][newy] = 1
            que.append([newx, newy, cnt + 1, myk])

if flg:
    print(mincnt)
else:
    print(-1)