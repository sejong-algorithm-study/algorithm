#G5 로봇 청소기 fail
dx = [-1, 0, 1, 0] #북 서 남 동
dy = [0, -1, 0, 1]#북 서 남 동

N, M  = map(int,input().split())

r, c, d = map(int, input().split())

area = []
for i in range(N):
    area.append(list(map(int, input().split())))
# 입력

# 방향 바꿔줘야함. 다른 깔끔한 방법 요구
if d == 1:
    d = 3
elif d == 3:
    d = 1

clean_cnt = 0

while True:
    area[r][c] = 2  #현재 위치 청소
    clean_cnt += 1

    cnt = 0
    while True:
        
        d += 1
        if cnt >= 4:
            # d
            if area[r - dx[(d - 1) % 4]][c - dy[(d - 1) % 4]] == 1:
                print(clean_cnt) 
                exit()
            # c
            r -= dx[(d - 1) % 4]
            c -= dy[(d - 1) % 4]
            cnt = 0
        # a
        if area[r + dx[d % 4]][c + dy[d % 4]] == 0:
            r += dx[d % 4]
            c += dy[d % 4]
            break

        # b
        else:
            cnt += 1# 4번 돌면 바뀔거임
            # print("2")
            continue