# 0부터 N 까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램을 작성
# dp[N][K]   = dp[0][K-1] + dp[1][K-1] + dp[2][K-1] + ... + dp[N-1][K-1] + dp[N][K-1]
# dp[N-1][K] = dp[0][K-1] + dp[1][K-1] + dp[2][K-1] + ... + dp[N-1][K-1]

# dp[N][K] = dp[N-1][K] + d[N][K-1]

N, K = map(int, input().split())
num = list(range(N + 1))

dp = [[0] * (K + 1) for _ in range(N + 1)]

# 0부터 N 까지 0 만드는 법은 1개
for i in range(K + 1):
    dp[0][i] = 1

for i in range(1, N + 1):
    for j in range(1, K + 1):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

print(dp[N][K] % 1000000000)
