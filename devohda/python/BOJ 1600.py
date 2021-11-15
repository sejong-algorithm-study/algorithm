from collections import deque

K = int(input())
h_dx = [1, 2, -1, -2, 1, 2, -1, -2]
h_dy = [2, 1, -2, -1, -2, -1, 2, 1]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 0, 0에서 시작
q = deque([(0, 0, 0, 0)])

# (H-1, W-1) 까지 가야 함
W, H = map(int, input().split())

# 체스판 만들기
board = []
for i in range(H):
    board.append(list(map(int, input().split())))

# 방문 처리
visited = [[[0 for _ in range(K + 1)] for _ in range(W)] for _ in range(H)]
visited[0][0][0] = 1


def check(nx, ny, h_move):
    if 0 <= nx < H and 0 <= ny < W:
        if visited[nx][ny][h_move] == 0 and board[nx][ny] != 1:
            return True
    return False


def move_monkey():
    while len(q):
        cx, cy, move, h_move = q.popleft()

        if cx == H - 1 and cy == W - 1:
            return move

        # 한 번 움직이기
        move += 1

        # 아직 말처럼 K번 안 움직였으면 말처럼 원숭이 움직이기
        if h_move < K:
            for i in range(8):
                nx, ny = cx + h_dx[i], cy + h_dy[i]
                if check(nx, ny, h_move + 1):
                    q.append((nx, ny, move, h_move + 1))
                    visited[nx][ny][h_move + 1] = 1

        # 원숭이 기본 움직이기
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if check(nx, ny, h_move):
                q.append((nx, ny, move, h_move))
                visited[nx][ny][h_move] = 1

    return -1


print(move_monkey())
