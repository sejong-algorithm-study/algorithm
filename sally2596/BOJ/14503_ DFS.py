import sys
cnt=0
setC =[-1,0,+1,0]
setR=[0,-1,0,1]
setD=[3,0,1,2]
backX=[1,0,-1,0]
backY=[0,-1,0,1]

def DFS( R, C, D):
    global cnt
    global arr

    afterR=R
    afterC=C
    afterD=D

    # 현재 위치 청소
    if arr[R][C] == 0:
        arr[R][C] = -1
        cnt = cnt+1

    for i in range(0,4,1):
        afterR=R+setR[afterD]
        afterC=C+setC[afterD]
        afterD=setD[afterD]

        if arr[afterR][afterC]!=0:
            continue
        #청소하지 않은 곳이라면 들어가기
        if arr[afterR][afterC]==0:
            DFS(afterR, afterC, afterD)
            return

    #후진 가능 불가능 파악하기
    if arr[R+backX[D]][C+backY[D]]==1:
        return
    else:
        DFS(R+backX[D], C+backY[D], D)


input = sys.stdin.readline
N, M = map(int, input().split())
R, C, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
DFS( R, C, D)
print(cnt)