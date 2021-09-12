import sys


def DP(arr,n):
    global  dp
    for i in range(1,n,1):
        for j in range(0,i,1):
            if arr[i]>arr[j] and dp[i]<dp[j]+1:
                dp[i]=dp[j]+1

input = sys.stdin.readline
n = int(sys.stdin.readline())
line = [int(sys.stdin.readline()) for i in range(n)]
dp=[1]*n
DP(line,n)
print(n-max(dp))