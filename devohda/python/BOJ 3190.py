from collections import deque

N = int(input())
K = int(input())

apple = []
for i in range(K):
    x, y = map(int, input().split())
    apple.append([x - 1, y - 1])

change = deque([])
L = int(input())
for i in range(L):
    X, C = input().split()
    change.append([int(X), C])

move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
snake = deque([[0, 0]])
direction = 0

cnt = 0
while True:
    cnt += 1
    head = snake[len(snake) - 1]
    new_head = [head[0] + move[direction][0], head[1] + move[direction][1]]

    # 종료 조건 - 벽에 부딪히거나 자기 자신에 부딪히면
    if new_head[0] == N or new_head[1] == N or new_head[0] == -1 or new_head[1] == -1:
        break
    elif new_head in snake:
        break

    if apple and new_head in apple:
        apple.pop(apple.index(new_head))  # 사과 먹기
    else:
        snake.popleft()  # 꼬리 비워주기
    snake.append(new_head)

    # 방향 전환
    if change and change[0][0] == cnt:
        if change[0][1] == 'L':
            direction -= 1
            if direction == -1:
                direction = 3
        else:
            direction += 1
            if direction == 4:
                direction = 0
        change.popleft()

print(cnt)
