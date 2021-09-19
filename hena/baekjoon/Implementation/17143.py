R, C, M = map(int, input().split())

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

shark = []

Map = [[0]* (C + 1) for _ in range(R + 1)]
for _ in range(M):
    r,c,s,d,z = map(int, input().split())
    Map[r][c] = z
    shark.append([r,c,s,d,z])

index = 0
ans = 0
# print("start")
while True:
    
    index += 1
    if index == C + 1:
        break

    # 상어 찾기
    x, y = 0, 0
    for i in range(1, R + 1):
        if Map[i][index] >= 1:
            x = i
            y = index
            ans += Map[i][index]
            Map[i][index] = 0
            break
    
    
    i = 0
    while i < len(shark):
        if shark[i][0] == x and shark[i][1] == y:
            del shark[i]
        else:
            Map[shark[i][0]][shark[i][1]] = 0
            i += 1 
    i = 0
    while i < len(shark):
        direction = shark[i][3]
        nx = shark[i][0] + dx[direction] * shark[i][2]
        ny = shark[i][1] + dy[direction] * shark[i][2]
        if direction == 1:
            nx = abs(shark[i][0] - R) - dx[direction] * shark[i][2]
            q, s = (nx) // (R - 1), (nx) % (R - 1)
            if q % 2 == 1:
                shark[i][3] = 2
                shark[i][0] = 1 + s
            else:
                shark[i][0] = R - s
            nx = shark[i][0]
        elif direction == 2:
            nx = shark[i][0] + dx[direction] * shark[i][2]
            q, s = (nx - 1) // (R - 1), (nx - 1) % (R - 1)
            if q % 2 == 1:
                shark[i][3] = 1
                shark[i][0] = R - s
            else:
                shark[i][0] = 1 + s
            nx = shark[i][0]
        # 우측 방향
        elif direction == 3:
            ny = shark[i][1] + dy[direction] * shark[i][2]
            q, s = (ny - 1) // (C - 1), (ny - 1) % (C - 1)
            if q % 2 == 1:
                shark[i][3] = 4
                shark[i][1] = C - s
            else:
                shark[i][1] = 1 + s
            ny = shark[i][1]
            
        # 좌측
        elif direction == 4:
            ny = abs(shark[i][1] - C) - dy[direction] * shark[i][2]
            q, s = (ny) // (C - 1), (ny) % (C - 1)
            if q % 2 == 1:
                shark[i][3] = 3
                shark[i][1] = 1 + s
            else:
                shark[i][1] = C - s
            ny = shark[i][1]
        if not Map[nx][ny]:
            Map[nx][ny] = shark[i][4]
        else:
            if Map[nx][ny] < shark[i][4]:
                Map[nx][ny] = shark[i][4]
        i += 1
    
    i = 0
    while i < len(shark):
        if Map[shark[i][0]][shark[i][1]] != shark[i][4]:
            del shark[i]
        else:
            i += 1