from collections import deque

N = int(input())
children = []
for _ in range(N):
    children.append(int(input()))

dp = [1 for i in range(N)]
for i in range(N):
    for j in range(i):
        if children[j] < children[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
