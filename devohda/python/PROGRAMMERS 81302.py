from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def is_close(x, y, lines):
    visited = [[False for _ in range(5)] for _ in range(5)]
    visited[x][y] = True

    q = deque([(x, y)])
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not (0 <= nx < 5 and 0 <= ny < 5):
                continue
            if visited[nx][ny] or distance(x, y, nx, ny) > 2 or lines[nx][ny] == 'X':
                continue
            if lines[nx][ny] == 'P':
                return True

            visited[nx][ny] = True
            q.append((nx, ny))
    return False


def distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


def solution(places):
    # 맨해튼 거리 2 이하 X => 주위(8자리)에 있으면 안 됨.
    answer = []
    for place in places:
        lines = []
        p_list = []
        for i in range(5):
            line = list(place[i])
            lines.append(line)

            for j in range(5):
                if line[j] == 'P':
                    p_list.append((i, j))

        # 앉은 자리 조사하기.
        flag = 1
        for x, y in p_list:
            if is_close(x, y, lines):
                flag = 0
                break

        answer.append(flag)

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
