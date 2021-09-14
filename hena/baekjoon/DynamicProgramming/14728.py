N, T = map(int, input().split())

array = [[0, 0]]
for _ in range(N):
    array.append(list(map(int, input().split())))

# print(array)
dp = [[0] * (T + 1) for _ in range(N + 1)]

for j in range(1, T + 1):
    if array[1][0] <= j:
        dp[1][j] = array[1][1]
    else:
        dp[1][j] = 0
# print(dp)

for i in range(2, N + 1):
    for j in range(1, T + 1):
        if j < array[i][0]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - array[i][0]] + array[i][1], dp[i - 1][j])
        
# print(dp)

# for i in range(1, N + 1):
#     for j in range(1, T + 1):
#         print(dp[i][j], end=" ")
#     print()
print(dp[N][T])