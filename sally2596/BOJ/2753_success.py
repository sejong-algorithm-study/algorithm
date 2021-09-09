from collections import deque
import sys
from copy import deepcopy

def sol(arr, N, M):
    locationque = findlocation(arr, N, M)
    count = 0

    while locationque:
        #빙산의 개수 확인
        if checkIceberg(locationque, arr, N, M)==0:
            return count
        else:
            count+=1
            #빙산 녹이기
            arr,locationque = melticeberg(locationque,arr,N,M)
            #print(locationque)


    return 0

def melticeberg(locationque,arr,N,M):
    temparr = deepcopy(arr)
    que = deque()

    while locationque:
        i,j=locationque.popleft()
        # 빙산의 변화는 다른 배열에 하기
        temparr[i][j] = melt(arr, i, j)

        # 녹이고도 0이 아니면 locationque에 추가
        if temparr[i][j] != 0:
            que.append([i, j])

    #print(que)


    return [temparr,que]

def melt(arr,i,j):
    cnt=0
    if arr[i + 1][j] == 0:
        cnt+=1
    if arr[i - 1][j] == 0:
        cnt+=1
    if arr[i][j + 1] == 0:
        cnt+=1
    if arr[i][j - 1] == 0:
        cnt+=1
    num= arr[i][j]-cnt
    if num<0:
        return 0
    return arr[i][j]-cnt

def checkIceberg(locationque, arr, N, M):
    que = deque([[locationque[0][0],locationque[0][1]]])

    visited =  [[0] * M for _ in range(N)]
    cnt = 0

    while que:
        i, j = que.popleft()

        if visited[i][j] == 1:
            continue
        cnt += 1
        visited[i][j] = 1
        #인접한 위치에 있는 빙산 찾기

        if arr[i+1][j]!=0 and visited[i+1][j]==0:
            que.append([i+1,j])
        if arr[i-1][j]!=0 and visited[i-1][j]==0:
            que.append([i-1,j])
        if arr[i][j+1]!=0 and visited[i][j+1]==0:
            que.append([i,j+1])
        if arr[i][j-1]!=0 and visited[i][j-1]==0:
            que.append([i,j-1])

    #빙산의 개수가 하나
    if cnt == len(locationque):
        return 1
    else: #빙산의 개수가 1개 이상임
        return 0


def findlocation(arr, N, M):
    que = deque()
    for i in range(1, N - 1, 1):
        for j in range(1, M - 1, 1):
            if arr[i][j] != 0:
                que.append([i, j])

    return que


input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(sol(arr, N, M))
