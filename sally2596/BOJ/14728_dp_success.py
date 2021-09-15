import sys
input = sys.stdin.readline
N, maxtime = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(maxtime+1)] for _ in range(N+1)]
def DP(time,i):
    if i== N or time>maxtime:
        return 0
    if dp[i][time]!=-1:
        return dp[i][time]
    if time+arr[i][0]<=maxtime:
        dp[i][time]=max(arr[i][1]+ DP(time+arr[i][0],i+1),DP(time,i+1))
    else:
        dp[i][time] = DP(time,i+1)
    return dp[i][time]

print(DP(0,0))

'''
import sys
input = sys.stdin.readline
N, maxtime = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [-1 for _ in range(maxtime+1)]
def DP(time,i):
    if i== N or time>maxtime:
        return 0
    if dp[time]!=-1:
        if time == arr[i][0] and dp[time]<arr[i][1]:
            dp[time]=arr[i][1]
        return dp[time]
    if time+arr[i][0]<=maxtime:
        dp[time]=max(arr[i][1]+ DP(time+arr[i][0],i+1),DP(time,i+1))
    else:
        dp[time] = DP(time,i+1)
    return dp[time]

print(DP(0,0))
'''