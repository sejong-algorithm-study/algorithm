from collections import deque
N = int(input())
Map = []

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 9:
            shark_i = i
            shark_j = j
    Map.append(tmp)
now_shark_size = 2


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
time = 0

def BFS(shark_i, shark_j, now_shark_size):
    queue = deque([[shark_i, shark_j]])
    visited = [[False] * N for _ in range(N)]

    visited[shark_i][shark_j] = True
    load_cnt = 0
    tmp = []
    while queue:
        
        # print("cnt",load_cnt)
        for _ in range(len(queue)):
            i, j = queue.popleft()
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or nx >= N or ny < 0  or ny >= N:
                    continue
                if Map[nx][ny] > now_shark_size:
                    visited[nx][ny] = True
                    continue
                if not visited[nx][ny]:
                    if Map[nx][ny] <= now_shark_size:
                        queue.append([nx, ny])
                    # print("hi")
                    if Map[nx][ny] < now_shark_size and Map[nx][ny]:
                        tmp.append((nx, ny, load_cnt + 1))
                        
                    visited[nx][ny] = True 
        load_cnt += 1        
    return tmp

def check(fishes):
    fishes.sort(key=lambda x: (x[2], x[0], x[1]))
    
    for fish in fishes:
        x, y, load = fish
        break
    return (x, y, load)

size_cnt = 0
Map[shark_i][shark_j] = 0
while True:
    fishes = BFS(shark_i, shark_j, now_shark_size)

    if not fishes:
        break
    shark_i, shark_j, load = check(fishes)
    size_cnt += 1
    if size_cnt == now_shark_size:
        now_shark_size += 1
        size_cnt = 0
    Map[shark_i][shark_j] = 0

    time += load
print(time)