from collections import deque
import heapq

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def solution(land, height):
    answer = 0
    n = len(land)
    visited = [[0 for i in range(n)] for _ in range(n)]
    heap =[[0,0,0]]
    while heap:
        length,x,y = heapq.heappop(heap)
        if visited[x][y]:
            continue
        visited[x][y]=1
        answer+=length
        for i in range(4):
            nowx = x + dx[i]
            nowy = y + dy[i]
            if 0<=nowx<n and 0<=nowy<n and visited[nowx][nowy]==0:
                if abs(abs(land[nowx][nowy])-abs(land[x][y]))>height:
                    heapq.heappush(heap,[abs(abs(land[nowx][nowy])-abs(land[x][y])),nowx,nowy])
                else:
                    heapq.heappush(heap,[0,nowx,nowy])
    return answer

print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]],1))