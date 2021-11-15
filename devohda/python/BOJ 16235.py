import sys

N, M, K = map(int, sys.stdin.readline().split())

land_fertile = []
for _ in range(N):
    land_fertile.append(list(map(int, sys.stdin.readline().split())))

trees = []
for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    trees.append((x - 1, y - 1, z))

# 나이 순으로 정렬
# sorted(trees, key=lambda tree: tree[2])

# 양분 처음에 모두 5
land = [[5 for _ in range(N)] for _ in range(N)]


def spring():
    new_trees = []
    for r, c, age in trees:
        if land[r][c] >= age:
            land[r][c] -= age
            new_trees.append((r, c, age + 1))
        else:
            die_trees.append((r, c, age))
    return new_trees


def summer():
    for r, c, age in die_trees:
        land[r][c] += age // 2


def fall():
    dx = [-1, 0, 1]
    dy = [-1, 0, 1]
    new_trees = []
    for r, c, age in trees:
        if age % 5 == 0:
            # 8개 돌기
            for i in range(3):
                for j in range(3):
                    if i == 1 and j == 1:
                        continue
                    nx, ny = r + dx[i], c + dy[j]
                    if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
                        new_trees.append((nx, ny, 1))
    return new_trees + trees


def winter():
    for i in range(N):
        for j in range(N):
            land[i][j] += land_fertile[i][j]


die_trees = []
# K 년 동안 나무 키우기

for _ in range(K):
    die_trees = []
    trees = spring()
    summer()
    trees = fall()
    winter()

print(len(trees))
