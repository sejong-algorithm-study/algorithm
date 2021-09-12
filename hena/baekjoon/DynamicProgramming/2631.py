N = int(input())
array = [0]
dp = [1] * (N + 1)
for _ in range(N):
    array.append(int(input()))
# print(array)
dp[0] = 0
for i in range(2, N + 1):
    for j in range(1, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N - max(dp))