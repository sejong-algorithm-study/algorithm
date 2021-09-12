N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
dp = [1] * N

for i in range(N):
    for j in range(i + 1, N):
        if arr[i] <= arr[j]:
            dp[j] = max(dp[j], dp[i] + 1)

print(N - max(dp))