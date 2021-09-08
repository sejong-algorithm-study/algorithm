from collections import deque


def go_to_startlink(floors, start, goal, up, down):
    visited = [False] * (F + 1)
    queue = deque([[start, 0]])

    while queue:
        now, cnt = queue.popleft()
        if now == goal:
            return cnt

        if visited[now]:
            continue

        visited[now] = True
        next_up = now + up
        next_down = now - down

        if next_up <= floors and not visited[next_up]:
            queue.append([next_up, cnt + 1])
        if next_down >= 1 and not visited[next_down]:
            queue.append([next_down, cnt + 1])

    return 'use the stairs'


F, S, G, U, D = map(int, input().split())
print(go_to_startlink(F, S, G, U, D))
