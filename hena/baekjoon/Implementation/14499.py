import sys
input = sys.stdin.readline
t, d, f, b, l, r = 0, 0, 0, 0, 0, 0
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
N, M, x, y, K = map(int , input().split())


def isPossible(x, y):
    if x < 0 or x >= N or y < 0 or y >=M:
        return False
    return True

def change(dir, value, t, d, f, b, l, r, nx, ny, Map):
    # not f b
    # 동쪽
    if dir == 1:
        # r, d, l, t = t, r, d, l
        t, r, d, l = l, t, r, d,
            
    elif dir == 2:
        # r, d, l, t = d, l, t, r
        t, r, d, l = r, d, l, t

    elif dir == 3:
        t, b, d, f = f, t, b, d
    elif dir == 4:
        t, b, d, f = b, d, f, t
    if Map[nx][ny]:
        d = value
        Map[nx][ny] = 0
    else:
        Map[nx][ny] = d
    return t, d, f, b, l, r

Map = []
for _ in range(N):
    Map.append(list(map(int, input().split())))

commands = list(map(int, input().split()))

for command in commands:
    nx = x + dx[command]
    ny = y + dy[command]
    if not isPossible(nx, ny):
        continue
    
    t, d, f, b, l, r = change(command, Map[nx][ny], t, d, f, b, l, r, nx, ny, Map)
    x = nx
    y = ny
    print(t)