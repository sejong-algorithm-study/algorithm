import sys
input = sys.stdin.readline
door_cnt = int(input())
left, right = map(int, input().split())
array = [0]
door = int(input())
for _ in range(door):
    array.append(int(input()))
dp = [[[int(1e9)]* (door_cnt + 1) for _ in range(door_cnt + 1)] for _ in range(door + 1)]
# print(dp)

# for open1 in range(door_cnt + 1):
#     for open2 in range(door_cnt + 1):
#         dp[0][open1][open2] = 0
dp[0][left][right] = 0
dp[0][right][left] = 0

for step in range(1, door + 1):
    index = array[step]
    for open1 in range(1, door_cnt + 1):
        for open2 in range(1, door_cnt + 1):
            dp[step][index][open2] = min(dp[step][index][open2], dp[step - 1][open1][open2] + abs(open1 - index))
            dp[step][open2][index] = min(dp[step][open2][index], dp[step - 1][open1][open2] + abs(open1 - index))

            dp[step][index][open1] = min(dp[step][index][open1], dp[step - 1][open1][open2] + abs(open2 - index))
            dp[step][open1][index] = min(dp[step][open1][index], dp[step - 1][open1][open2] + abs(open2 - index))
ans = int(1e9)
for i in range(1, door_cnt + 1):
    for j in range(i + 1, door_cnt + 1):
        ans = min(ans, dp[door][i][j])
print(ans)    


# def count(index, open1, open2): 
#     # print(index, open1, open2)
#     if index == door + 1:
#         # print("index,l,r",index, open1, open2)
#         # print("val:", dp[index][open1][open2])
#         return 0
#     # print(index)
#     target = array[index]
#     dp[index][open1][open2] = min(abs(open1 - target) + count(index + 1, target, open2), abs(open2 - target) + count(index + 1, open1, target))
#     return dp[index][open1][open2]
# print(count(1, left, right))
