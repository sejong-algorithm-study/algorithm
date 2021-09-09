from collections import deque
import sys
def sol(arr,N,M):
    cnt = 0
    que = makeset(arr, N, M)

    while len(que)!=0:
        cnt+=1
        #없어진 빙산 list 삭제
        for i in range(len(que)-1,-1,-1):
            if que[i][0]==0:
                que.remove(que[i])

        if len(que)==0:
            return 0
        #몇덩이인지 검사
        #덩이 분리 : 0 한덩이:1
        if BFS(que) == 0:
            return cnt
        else:
            que = remake(que)
    return 0

def remake(originque):
    que=originque
    for i in range(len(originque)):
        x = originque[i][1][0]
        y = originque[i][1][1]

        after = originque[i][0]-(4-len(list(filter(lambda k: (originque[k][1][0] == x + 1 and originque[k][1][1] == y) or (
                originque[k][1][0] == x - 1 and originque[k][1][1] == y) or (
                                          originque[k][1][0] == x and originque[k][1][1] == y + 1) or (
                                          originque[k][1][0] == x and originque[k][1][1] == y - 1),
                        range(len(originque))))))
        if after<0:
            after = 0
        que[i][0]=after

    return originque
def BFS(originque):
    tempque=[]
    tempque.append([originque[0],0])

    visited =[0]*len(originque)

    while tempque:
        data,current = tempque.pop(0)

        visited[current]=1
        x=data[1][0]
        y=data[1][1]

        index = list(filter(lambda k: (originque[k][1][0] == x+1 and originque[k][1][1] == y)or (originque[k][1][0] == x-1 and originque[k][1][1] == y) or (originque[k][1][0] == x and originque[k][1][1] == y+1) or (originque[k][1][0] == x and originque[k][1][1] == y-1), range(len(originque))))

        for j in index:
            if visited[j]==0:
                visited[j]=1
                tempque.append([originque[j],j])

    if 0 in visited:
        return 0
    else:
        return 1

def makeset(arr,N,M):
    list =[]
    for i in range(1,N-1,1):
        for j in range(1,M-1,1):
            if arr[i][j]==0:
                continue
            else:
                q = check(arr,i,j)
                list.append(q)

    return list



def check(iceberg,i,j):
    loc=[i,j]
    after = arr[i][j] - counticeberg(arr,i,j)
    if after<=0:
        after =0

    return [after,loc]

def counticeberg(arr,i,j):
    cnt =0
    if arr[i-1][j]==0:
        cnt+=1
    if arr[i+1][j]==0:
        cnt+=1
    if arr[i][j-1]==0:
        cnt+=1
    if arr[i][j+1]==0:
        cnt+=1
    return cnt

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(sol(arr,N,M))
