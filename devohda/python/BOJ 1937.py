import sys

sys.setrecursionlimit(100000)

# 욕심쟁이 판다
N = int(input())

# 대나무 숲 만들기
bamboo = []
for _ in range(N):
    bamboo.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dp = [[0 for _ in range(N)] for _ in range(N)]


# 판다의 위치 돌면서 판다 가장 긴 경로 찾기(DFS)
def dfs(x, y):
    # 이미 방문한 곳이면 반환
    if dp[x][y]:
        return dp[x][y]
    else:
        # 방문 처리
        dp[x][y] = 1

        # 사방에 대나무를 돌면서 대나무가 많은 장소가 있다면 이동
        # 없으면 그 자리에서 죽음
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if bamboo[nx][ny] > bamboo[x][y]:
                    dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
        return dp[x][y]


answer = 0
for i in range(N):
    for j in range(N):
        answer = max(answer, dfs(i, j))

print(answer)
