import sys

n, k = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [0] * (k + 1)

for i in range(n):
    for j in range(k, 0, -1):
        if arr[i][0]<= k:
            dp[j] = max(dp[j], dp[j-arr[i][0]] + arr[i][1] if j-arr[i][0]>=0 else 0)

print(max(dp))
