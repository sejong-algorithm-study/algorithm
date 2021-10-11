import sys
from collections import deque
n,m,x,y,k = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
arr = list(map(int, sys.stdin.readline().split()))

dx=[0,0,-1,1]
dy =[1,-1,0,0]
dice = [0,0,0,0,0,0]

que1 = deque([0,1,2,4])
que2 = deque([5,1,3,4])

def movedice(dir):
    if dir == 0:
        que1.appendleft(que1.pop())
        que2[1]= que1[1]
        que2[3]=que1[3]
    elif dir ==1:
        que1.append(que1.popleft())
        que2[1] = que1[1]
        que2[3] = que1[3]
    elif dir==2:
        que2.append(que2.popleft())
        que1[1] = que2[1]
        que1[3] = que2[3]
    else:
        que2.appendleft(que2.pop())
        que1[1] = que2[1]
        que1[3] = que2[3]

for i in range(k):
    direction = arr[i]-1
    nextx = x + dx[direction]
    nexty = y + dy[direction]
    if 0<=nextx<n and 0<=nexty<m:#범위 안에 있을때
        movedice(direction)
        top = que2[1]
        bottom =que2[3]
        if board[nextx][nexty]==0:
            board[nextx][nexty] = dice[bottom]
        else:
            dice[bottom] = board[nextx][nexty]
            board[nextx][nexty] = 0
        print(dice[top])
        x=nextx
        y=nexty