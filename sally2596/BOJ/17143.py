import sys
R, C,M = map(int, sys.stdin.readline().split())
shark = [[0]*C for i in range(R)]
for i in range(M):
    r,c,s,d,z = map(int, sys.stdin.readline().split())
    shark[r-1][c-1] = [s,d,z]

mover=[-1,1,0,0]
movec=[0,0,1,-1]
def moveshark():
    tempshark = [[0]*C for i in range(R)]
    for i in range(R):
        for j in range(C):
            if shark[i][j]!=0: #상어가 있으면 이동시키기
                r,c,s,d,z = i,j,shark[i][j][0],shark[i][j][1],shark[i][j][2]
                while s>0: #속력이 있을 경우 이동 조치
                    r+=mover[d-1]
                    c+=movec[d-1]
                    if 0 <= r < R and 0 <= c < C: #범위 안에 있으면
                        s-=1
                    else: #범위 벗어나면 방향 바꾸기
                        r -= mover[d-1]
                        c -= movec[d-1]
                        if d == 1:
                            d = 2
                        elif d == 2:
                            d = 1
                        elif d == 3:
                            d = 4
                        elif d == 4:
                            d = 3


                if tempshark[r][c] == 0:
                    tempshark[r][c] = [shark[i][j][0], d, z]
                else:
                    if tempshark[r][c][2] < z:
                        tempshark[r][c] = [shark[i][j][0], d, z]

    return tempshark

total = 0
for i in range(C):
    for j in range(R):
        if shark[j][i]!=0:
            total += shark[j][i][2]
            shark[j][i]=0 #상어 삭제
            break
    shark = moveshark()
print(total)