R, C = map(int, input().split())

alpha = [False] * 26
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0
maxVal = 0

def DFS(Map, alpha, x, y, cnt):
    global maxVal
    value = Map[x][y]
    if cnt > maxVal:
        maxVal = cnt

    # 참으로 바꾸기
    alpha[ord(value) - ord('A')] = True

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if not alpha[ord(Map[nx][ny]) - ord('A')]:
            DFS(Map, alpha, nx, ny, cnt + 1)
            alpha[ord(Map[nx][ny]) - ord('A')] = False
Map = []
for _ in range(R):
    Map.append(list(map(str, input())))
DFS(Map, alpha, 0, 0, cnt)
print(maxVal + 1)


