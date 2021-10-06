import sys
n,m = map(int,sys.stdin.readline().split())
chicken =[]
home=[]
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            home.append([i,j])
        elif arr[i][j]==2:
            chicken.append([i,j])

len_chicken = len(chicken)
visited = [0]*len_chicken
len_home = len(home)
result = n*n*n

def DFS(now,cnt):
    global result
    if cnt==m:
        distance = [n+n+1]*len_home
        for i in range(len_home):
            for j in range(len_chicken):
                if visited[j]:
                    distance[i] = min(distance[i],abs(chicken[j][0]-home[i][0])+abs(chicken[j][1]-home[i][1]))
        result = min(result,sum(distance))

    if now ==len_chicken:
        return
    visited[now] = 1
    DFS(now+1,cnt+1)
    visited[now]=0
    DFS(now + 1, cnt)

DFS(0,0)
print(result)


