import sys
from collections import deque

n,m,k = map(int,sys.stdin.readline().split())
feed =[[5]*n for _ in range(n)]
newfeed = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
tree = [[deque([]) for q in range(n)] for _ in range(n)]
dietree=deque([])
for i in range(m):
    x,y,year = map(int,sys.stdin.readline().split())
    tree[x-1][y-1].append(year)

def spring():
    for x in range(n):
        for y in range(n):
            if tree[x][y]:
                newtree = deque([])
                while tree[x][y]:
                    treeage = tree[x][y].popleft()
                    if treeage <= feed[x][y]:
                        feed[x][y] -= treeage
                        newtree.append(treeage + 1)
                    else:
                        dietree.append([x, y, treeage])
                tree[x][y] = newtree  # 트리 힙 바꾸기


def summer():
    while dietree:
        x,y,age = dietree.pop()
        feed[x][y]+=age//2


dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]

def fall():
    for x in range(n):
        for y in range(n):
            for treeage in tree[x][y]:
                if treeage % 5 == 0:
                    for i in range(8):
                        newx = x+dx[i]
                        newy = y+dy[i]
                        if 0 <= newx < n and 0 <= newy < n:
                            tree[newx][newy].appendleft(1)

def winter():
    for i in range(n):
        for j in range(n):
            feed[i][j]+=newfeed[i][j]

for i in range(k):
    spring()
    summer()
    fall()
    winter()

cnt=0
for x in range(n):
    for y in range(n):
        cnt+= len(tree[x][y])
print(cnt)