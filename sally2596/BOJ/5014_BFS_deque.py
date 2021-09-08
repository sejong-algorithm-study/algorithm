from collections import deque


def soulution(F, S, G, U, D):
    que = deque([S, 0])

    visited = [0] * (F + 1)

    while que:
        current, cnt = que.popleft()
        if current == G:
            return cnt

        if visited[current] == 1:
            continue

        visited[current] = 1

        if current + U <= F and visited[current + U] == 0:
            que.append([current + U, cnt + 1])

        if current - D > 0 and visited[current - D] == 0:
            que.append([current - D, cnt + 1])

    return "use the stairs"

F, S, G, U, D = input().split(" ")
print(soulution(int(F), int(S), int(G), int(U), int(D)))
