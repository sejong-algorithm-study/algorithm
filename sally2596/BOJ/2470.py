import sys
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
s = 0
e = n-1
maxnow = sys.maxsize
nows =0
nowe = n-1
while s<e:
    now = arr[s]+arr[e]
    if abs(maxnow)>abs(now):
        nows= s
        nowe = e
        maxnow = now
        if now==0:
            break
    if now<0:
        s+=1
    elif now>0:
        e-=1
print(arr[nows],arr[nowe])
