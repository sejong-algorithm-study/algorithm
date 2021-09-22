import sys

R, C = map(int, sys.stdin.readline().split())
arr = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(R)]
visited = [0] * 26

maxcnt = 0


def DFS(i, j, cnt):
    global maxcnt
    if visited[ord(arr[i][j]) - ord("A")] == 1:
        return
    else:
        visited[ord(arr[i][j]) - ord("A")] = 1

    if cnt > maxcnt:
        maxcnt = cnt

    if j + 1 < C and visited[ord(arr[i][j + 1]) - ord("A")] == 0:
        DFS(i, j + 1, cnt + 1)
        visited[ord(arr[i][j + 1]) - ord("A")] = 0  # 빠져나오면서 방문 안한상태로 바꾸기
    if i + 1 < R and visited[ord(arr[i + 1][j]) - ord("A")] == 0:
        DFS(i + 1, j, cnt + 1)
        visited[ord(arr[i + 1][j]) - ord("A")] = 0
    if j - 1 >= 0 and visited[ord(arr[i][j - 1]) - ord("A")] == 0:
        DFS(i, j - 1, cnt + 1)
        visited[ord(arr[i][j - 1]) - ord("A")] = 0
    if i - 1 >= 0 and visited[ord(arr[i - 1][j]) - ord("A")] == 0:
        DFS(i - 1, j, cnt + 1)
        visited[ord(arr[i - 1][j]) - ord("A")] = 0

DFS(0,0,1)
print(maxcnt)
