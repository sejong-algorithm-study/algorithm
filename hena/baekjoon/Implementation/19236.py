dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def fish_possible(nx, ny, shark_i, shark_j):
    # print(nx, ny, shark_i, shark_j)
    if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
        return False
    if nx == shark_i and ny == shark_j:
        return False
    return True

def find_fish(value, Map):
    for i in range(4):
        for j in range(4):
            if Map[i][j] and Map[i][j][0] == value[2]:
                return (i , j)

def printf(Map):
    print("start")
    for i in range(4):
        for j in range(4):
            print(Map[i][j], end=" ")
        print()
    print("end")
# 기본 좌표
x, y = 0, 0
fishes = []


# 기본 세팅이 거지같;
for i in range(4):
    setting = list(map(int, input().split()))
    for index in range(1,5):
        size, direction = setting[2 * (index - 1) : 2 * index]
        fishes.append([x, y, size, direction - 1])
        y += 1
        if y > 3:
            y %= 4
            x += 1
fishes.sort(key=lambda x: (x[2]))

total = 0

Map = [[0]* 4 for _ in range(4)]
for fish in fishes:
    x, y, size, direction = fish
    Map[x][y] = [size, direction]
shark_i, shark_j = 0, 0
shark_direction = Map[shark_i][shark_j][1]


Max = 0



def save_fish(fishes, Map):
    for i in range(4):
        for j in range(4):
            if Map[i][j]:
                fishes.append([i, j, Map[i][j][0], Map[i][j][1]])
    fishes.sort(key=lambda x:(x[2]))

def recover(Map, fishes):
    for i in range(4):
        for j in range(4):
            Map[i][j] = 0
    for fish in fishes:
        i, j, size, dir= fish
        Map[i][j] = [size, dir]

def recursive(Map, shark_i, shark_j, shark_direction, total):
    global Max
    # print("shark",shark_i, shark_j, shark_direction,total)
    # 저장용
    shark = [shark_i, shark_j, shark_direction] 
    fishes = []
    
    
    # 상어가 먹음 아래서 예외처리하기
    total += Map[shark_i][shark_j][0]
    if total > Max:
        Max = total
    Map[shark_i][shark_j] = 0
    save_fish(fishes, Map)
    for fish in fishes:
        #물고기 찾아라
        
        x, y = find_fish(fish, Map)
        for k in range(8):
            direction = fish[3]
            nx, ny = x + dx[(direction + k) % 8], y + dy[(direction + k) % 8]
            if not fish_possible(nx, ny, shark_i, shark_j):
                continue
            else:
                Map[x][y][1] = (direction + k) % 8
                Map[nx][ny], Map[x][y] = Map[x][y], Map[nx][ny]
                break

    # print("before fish",fishes)
    fishes.clear()
    save_fish(fishes, Map)
    # print("after fish",fishes)
    # print("here")
    # printf(Map)

    sharkposition = []
    for k in range(1,4):
        new_i = shark_i + dx[shark_direction] * k
        new_j = shark_j + dy[shark_direction] * k
        if new_i < 0  or new_i >= 4 or new_j < 0  or new_j >= 4:
            continue
        if not Map[new_i][new_j]:
            continue
        sharkposition.append([new_i, new_j, Map[new_i][new_j][1]])
    # for k in sharkposition:
    while sharkposition:
        x, y, dir = sharkposition.pop()
        # x, y, dir = k
        recursive(Map, x, y, dir, total)
        recover(Map, fishes)
    return

# printf(Map)
# print("main start")
recursive(Map, shark_i, shark_j, shark_direction, 0)
# print("main end")
print(Max)