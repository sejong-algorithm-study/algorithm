from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(m, n, picture):
    area = 0
    max_area = 0
    for i in range(m):
        for j in range(n):
            if picture[i][j] == 0:
                continue

            area += 1
            cur_area = 0
            q = deque([(i, j)])
            color = picture[i][j]
            picture[i][j] = 0

            while q:
                c_x, c_y = q.popleft()
                cur_area += 1

                for k in range(4):
                    m_x, m_y = c_x + dx[k], c_y + dy[k]
                    if 0 <= m_x < m and 0 <= m_y < n:
                        if picture[m_x][m_y] == color:
                            picture[m_x][m_y] = 0
                            q.append((m_x, m_y))

            max_area = max(max_area, cur_area)

    return [area, max_area]


m = int(input())
n = int(input())
picture = []
for _ in range(m):
    picture.append(list(map(int, input().split(', '))))

print(solution(m, n, picture))