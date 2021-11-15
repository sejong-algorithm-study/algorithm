from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())

# 치즈 입력 받기
# 치즈는 전역 변수
cheese = []
is_cheese = deque([])
for i in range(N):
    cheese_row = list(map(int, input().split()))
    cheese.append(cheese_row)
    for j in range(M):
        if cheese[i][j] == 1:
            is_cheese.append((i, j))

cnt = 0
corner_cheese = []
visit_outer_cheese = False


# 치즈 내부 공기인지 확인
def is_inner_cheese(x, y):
    # 이미 방문했는지 확인
    if visited[x][y] == 1:
        return False
    elif visited[x][y] == 2:
        return True

    visited[x][y] = 1

    visit_cheese = []
    tmp_q = deque([(x, y)])
    out_of_range = False
    # 방문 안 한 곳이면 bfs 로 방문처리
    while len(tmp_q):
        tx, ty = tmp_q.popleft()
        visit_cheese.append((tx, ty))
        for k in range(4):
            nx = tx + dx[k]
            ny = ty + dy[k]
            if not (0 <= nx < N and 0 <= ny < M):
                out_of_range = True
                continue

            if cheese[nx][ny] == 1 or visited[nx][ny] != 0:
                continue

            visited[nx][ny] = 1
            tmp_q.append((nx, ny))

    # 내부 공기는 방문 처리하기
    if not out_of_range:
        for vx, vy in visit_cheese:
            visited[vx][vy] = 2
        return True
    else:
        return False


while True:
    cnt += 1
    tmp = deque([])
    # 방문 안 했으면 0, 방문했는데 외부 공기면 1, 방문했는데 내부 공기면 2
    visited = [[0 for _ in range(M)] for _ in range(N)]
    while len(is_cheese):
        cx, cy = is_cheese.popleft()
        flag = 0
        for i in range(4):
            mx, my = cx + dx[i], cy + dy[i]
            # 옆이 0이면서 치즈 내부 공기가 아닌 경우엔 flag 증가
            if cheese[mx][my] == 1:
                continue

            if not is_inner_cheese(mx, my):
                flag += 1

        # 네 방향 중 2개 이상이 외부 공기이면 녹아야 하는 부분이므로 큐에 추가
        if flag >= 2:
            corner_cheese.append((cx, cy))
        else:
            tmp.append((cx, cy))

    # 치즈 녹이기
    for rm_x, rm_y in corner_cheese:
        cheese[rm_x][rm_y] = 0

    # 더이상 치즈가 없으면(다 녹았으면)
    if len(tmp) == 0:
        break

    is_cheese = tmp

print(cnt)
