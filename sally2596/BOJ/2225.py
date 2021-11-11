import sys
n,k = map(int,sys.stdin.readline().split())
arr=[[1]*(n+1) for _ in range(k)]
for i in range(1,k):
    for j in range(1,n+1):
        arr[i][j] = arr[i-1][j]+arr[i][j-1]
print(arr[-1][-1]%1000000000)
