import sys
sys.setrecursionlimit(100000)
n = int(input())
dp = [[[-1 for _ in range(4)] for _ in range(3)] for _ in range(n)]
cnt = 0

def attendance(day, late, absent):
    global dp
    if late >= 2 or absent >= 3:
        return 0

    if day == n:
        return 1

    if dp[day][late][absent] != -1:
        return dp[day][late][absent]

    dp[day][late][absent] = int((attendance(day + 1, late, 0) + attendance(day + 1, late + 1, 0) + attendance(day + 1, late, absent + 1))%1,000,000)
    return dp[day][late][absent]


print(attendance(0, 0, 0))
