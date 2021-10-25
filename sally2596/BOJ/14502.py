import sys
import copy
from collections import deque

n,m = map(int,sys.stdin.readline().split())
arr=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
maxcnt=0
que = deque([])
dx=[1,0,-1,0]
dy=[0,-1,0,1]

def check():
    cnt=0
    nowarr = copy.deepcopy(arr)
    for i in range(n):
        for j in range(m):
            if nowarr[i][j] == 2:
                que.append([i, j])
    while que:
        i,j = que.popleft()
        for k in range(4):
            x = i+dx[k]
            y = j+dy[k]
            if 0<=x<n and 0<=y<m and nowarr[x][y]==0:
                nowarr[x][y]=2
                que.append([x,y])
    for i in range(n):
        for j in range(m):
            if nowarr[i][j]==0:
                cnt+=1
    return cnt

def DFS(cnt):
    global maxcnt
    if cnt==3:
        maxcnt = max(maxcnt,check())
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j]=1
                DFS(cnt+1)
                arr[i][j]=0

DFS(0)
print(maxcnt)