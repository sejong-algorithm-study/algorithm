import copy

N, M = map(int, input().split())

# 확인할 방향
check = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]
room = []
cctv = []

for i in range(N):
    room.append(list(map(int, input().split())))
    for j in range(M):
        if 1 <= room[i][j] <= 5:
            # cctv 있으면 저장
            cctv.append([room[i][j], i, j])


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# cctv 감시 범위 검사
def check_room(tmp, direction, x, y):
    for i in direction:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                break
            if tmp[nx][ny] == 6:
                break
            elif tmp[nx][ny] == 0:
                tmp[nx][ny] = 7


def dfs(idx, arr):
    global min_value

    # 전체 다 검사했으면
    if idx == len(cctv):
        count = 0
        for i in range(N):
            count += arr[i].count(0)
        min_value = min(min_value, count)
        return

    tmp = copy.deepcopy(arr)

    # cctv 종류에 따라서 검사하기
    cctv_type, x, y = cctv[idx]
    for i in check[cctv_type]:
        check_room(tmp, i, x, y)
        dfs(idx + 1, tmp)
        tmp = copy.deepcopy(arr)


min_value = int(1e9)
dfs(0, room)
print(min_value)
