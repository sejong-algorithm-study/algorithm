import sys
from collections import deque
import copy

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            shark_i = i
            shark_j = j
            arr[i][j]=0
            break

shark_weight = 2

total = 0


def bfs():
    que = deque([[(shark_i, shark_j), 0]])
    visited = [[0] * n for i in range(n)]
    caneat =[]

    while que:
        (ii, jj), distance = que.popleft()
        for i in range(4):
            ni, nj = ii + di[i], jj + dj[i]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][
                    nj] == 0:  # 인덱스 범위 안 & 방문 안한 경우에
                if arr[ni][nj] <= shark_weight:  #지나갈 수 있는 경우
                    que.append([(ni, nj), distance + 1])
                    visited[ni][nj] = 1
                    if arr[ni][nj] != 0 and arr[ni][nj] < shark_weight:
                        caneat.append([distance+1, ni, nj])

    if caneat:
        caneat.sort()
        return caneat[0]
    else:
        return None

count = 0
while True:
    target = bfs()
    if target == None:
        break
    else:
        dis, i, j = target[0], target[1], target[2]
        count+=1
        if count == shark_weight:
            shark_weight += 1
            count = 0
        total += dis
        arr[i][j] = 0
        shark_i, shark_j = i, j
print(total)
