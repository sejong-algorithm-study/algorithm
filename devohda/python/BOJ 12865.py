N, K = map(int, input().split())

obj = []
for _ in range(N):
    # W, V 받기
    obj.append(list(map(int, input().split())))

dp = [[0 for i in range(K + 1)] for K in range(N + 1)]
for i in range(N):
    for j in range(K):
        W = obj[i][0]
        V = obj[i][1]

        if j <= W:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - W] + V)

print(dp[N-1][K-1])
