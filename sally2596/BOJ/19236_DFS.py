import sys
import copy

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

arr = [list(map(int, sys.stdin.readline().split())) for i in range(4)]

tank = [[0]*4 for i in range(4)] #물고기 위치 수조
fish={} #물고기 정보 담은 딕셔너리

# 물고기 정보를 fish배열에 담기
for i in range(4):
    for j in range(4):
        tank[i][j] = arr[i][2*j]
        fish[arr[i][2*j]]=[i,j,arr[i][2*j+1]-1]


def movefish(fish,tank):
    for i in range(16):
        if fish[i+1]==-1:
            continue
        y, x ,direction = fish[i+1]
        for j in range(8):
            direction = (fish[i+1][2]+j)%8 # 방향 1개씩 움직이기
            ny = y+dy[direction] #바뀔 물고기의 위치
            nx = x +dx[direction]
            if 0<=nx<4 and 0<=ny<4 and tank[ny][nx]!=-1:# 범위 안에 있으면서 움직일 위치에 물고기가 있따면
                index = tank[ny][nx]
                if index!=0:
                    fish[index]= [y,x,fish[index][2]]
                fish[i+1] = [ny,nx,direction]
                tank[ny][nx] = i+1
                tank[y][x] =index
                break
    return fish, tank

shark_i = shark_j = 0
total = tank[shark_i][shark_j]
shark_dir = fish[tank[shark_i][shark_j]][2]
fish[tank[shark_i][shark_j]]=-1
tank[shark_i][shark_j]=0 # 상어가 먹음
answer = 0

def DFS(ny,nx,fish,tank,dir,total):
    global answer
    tank[ny][nx]=-1
    fish,tank = movefish(fish,tank)

    for i in range(1,4):
        newy = ny + dy[dir]*i
        newx = nx + dx[dir]*i
        if 0<=newx<4 and 0<=newy<4 and tank[newy][newx]!=0:
            temp = tank[newy][newx]
            tempdir = fish[tank[newy][newx]][2]
            tempfish = copy.deepcopy(fish)
            temptank = copy.deepcopy(tank)
            fish[tank[newy][newx]] = -1
            tank[ny][nx] = 0
            DFS(newy,newx,fish,tank,tempdir,total+temp)
            fish = tempfish
            tank =temptank
    if total> answer:
        answer = total
DFS(0,0,fish,tank,shark_dir,total)
print(answer)