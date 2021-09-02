dp = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(len(dp))
for i in range(1, 5):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] += dp[i - 1][j]
        elif j == i:
            dp[i][j] += dp[i - 1][j - 1]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + dp[i][j]
    print(dp[i])
print(dp)

# 7
# 3   8
# 8   1   0
# 2   7   4   4
# 4   5   2   6   5
