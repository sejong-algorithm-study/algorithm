import sys
from collections import deque
import copy

n,m = map(int,sys.stdin.readline().split())
arr= [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

que = deque([])
dx= [0,1,0,-1]
dy=[1,0,-1,0]


def outside(num):
    global arr
    visited = [[0 for i in range(m)] for j in range(n)]
    flag = False
    out = deque([])
    for i in range(n):
        for j in range(m):
            if arr[i][j]==num:
                visited[i][j] = 1
                out.append([i, j])
                flag=True
                break
        if flag:
            break
    while out:
        x,y= out.popleft()
        for i in range(4):
            nowx = x + dx[i]
            nowy = y +dy[i]
            if 0<=nowx<n and 0<=nowy<m and visited[nowx][nowy]==0 and (arr[nowx][nowy]==0 or arr[nowx][nowy]==num):
                arr[nowx][nowy]=-1
                visited[nowx][nowy]=1
                out.append([nowx,nowy])

def BFS():
    global arr
    tmparr = copy.deepcopy(arr)
    tmpque = deque([])
    for j in range(n):
        for k in range(m):
            tmp = 0
            for i in range(4):
                nowx = j + dx[i]
                nowy = k + dy[i]
                if 0 <= nowx < n and 0 <= nowy < m and arr[nowx][nowy] == -1:
                    tmp += 1
            if tmp >= 2:
                tmparr[j][k] = -1
            elif tmparr[j][k]==1:
                tmpque.append([j, k])
    arr= copy.deepcopy(tmparr)
    outside(-1)
    return tmpque

cnt=0
outside(0)
while True:
    cnt += 1
    que = BFS()
    if not que:
        break
print(cnt)
