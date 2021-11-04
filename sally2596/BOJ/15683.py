import sys
import copy

n,m = map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dx=[1,0,-1,0]
dy=[0,-1,0,1]

cctv =[]
direction=[]

for i in range(n):
    for j in range(m):
        if 1<=arr[i][j]<=5:
            cctv.append([arr[i][j],i,j])

maxnum = n*m

def check(tmparr):
    cnt=0
    for i in range(n):
        for j in range(m):
            if tmparr[i][j]==0:
                cnt+=1
    return cnt

def look(x,y,dir,tmparr):
    newx = x + dx[dir]
    newy = y + dy[dir]
    while 0 <= newx < n and 0 <= newy < m and tmparr[newx][newy] != 6:
        if tmparr[newx][newy] == 0:
            tmparr[newx][newy] = -1
        newx = newx + dx[dir]
        newy = newy + dy[dir]
    return tmparr

def DFS(depth):
    global maxnum
    if depth == len(cctv):
        tmparr = copy.deepcopy(arr)
        for i in range(len(cctv)):
            num,x,y =cctv[i][0],cctv[i][1],cctv[i][2]
            dir = direction[i]
            if num==1:
                tmparr = look(x,y,dir,tmparr)
            elif num == 2:
                tmparr = look(x, y, dir, tmparr)
                tmparr = look(x, y, dir+2, tmparr)
            elif num==3:
                if dir ==0:
                    tmparr = look(x, y, 0, tmparr)
                    tmparr = look(x, y, 1, tmparr)
                elif dir ==1:
                    tmparr = look(x, y, 1, tmparr)
                    tmparr = look(x, y, 2, tmparr)
                elif dir ==2:
                    tmparr = look(x, y, 2, tmparr)
                    tmparr = look(x, y, 3, tmparr)
                elif dir==3:
                    tmparr = look(x, y, 0, tmparr)
                    tmparr = look(x, y, 3, tmparr)
            elif num==4:
                if dir == 0:
                    tmparr = look(x, y, 0, tmparr)
                    tmparr = look(x, y, 1, tmparr)
                    tmparr = look(x, y, 2, tmparr)
                elif dir == 1:
                    tmparr = look(x, y, 1, tmparr)
                    tmparr = look(x, y, 2, tmparr)
                    tmparr = look(x, y, 3, tmparr)
                elif dir == 2:
                    tmparr = look(x, y, 2, tmparr)
                    tmparr = look(x, y, 3, tmparr)
                    tmparr = look(x, y, 0, tmparr)
                elif dir == 3:
                    tmparr = look(x, y, 0, tmparr)
                    tmparr = look(x, y, 1, tmparr)
                    tmparr = look(x, y, 3, tmparr)
            elif num==5:
                tmparr = look(x, y, 0, tmparr)
                tmparr = look(x, y, 1, tmparr)
                tmparr = look(x, y, 2, tmparr)
                tmparr = look(x, y, 3, tmparr)
        maxnum = min(check(tmparr),maxnum)


        return
    if cctv[depth][0]==1 or cctv[depth][0]==3 or cctv[depth][0]==4:
        for i in range(4):
            direction.append(i)
            DFS(depth+1)
            direction.pop()
    elif cctv[depth][0]==2:
        for i in range(2):
            direction.append(i)
            DFS(depth + 1)
            direction.pop()
    else:
        direction.append(0)
        DFS(depth + 1)
        direction.pop()

DFS(0)
print(maxnum)