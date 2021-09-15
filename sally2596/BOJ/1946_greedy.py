import sys
N = int(sys.stdin.readline())
for i in range(N):
    arr = []
    cnt=0
    M = int(input())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    arr.sort()
    minnum = arr[0][1]
    for j in range(1,len(arr)):
        if arr[j][1]<minnum:
            minnum = arr[j][1]
            cnt+=1
    print(cnt+1)