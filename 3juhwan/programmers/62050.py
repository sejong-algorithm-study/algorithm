from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


# 특정 원소가 속한 집합을 찾기
def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기 (간선 연결한다고 생각!)
def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB


def numbering(land, numbered, height):
    n = len(land)

    def bfs(x, y, number):
        q = deque([(x, y)])
        numbered[x][y] = number
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if not numbered[nx][ny] and abs(land[x][y]-land[nx][ny]) <= height:
                        numbered[nx][ny] = number
                        q.append((nx, ny))

    number = 1
    for i in range(n):
        for j in range(n):
            if not numbered[i][j]:
                bfs(i, j, number)
                number += 1

    return number       # 마지막 숫자 + 1


def getAdjGraph(land, numbered):
    n = len(land)
    adjList = []
    for x in range(n):
        for y in range(n):
            for i in range(2, 4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    a, b = numbered[x][y], numbered[nx][ny]
                    if a != b:
                        adjList.append((abs(land[x][y]-land[nx][ny]), a, b))
    return adjList


def solution(land, height):
    n = len(land)
    numbered = [[0]*n for __ in range(n)]

    nlen = numbering(land, numbered, height)

    adjList = getAdjGraph(land, numbered)
    adjList.sort()


    parent = [0] * (nlen + 1)
    answer = 0

    # 부모 테이블상에서, 부모를 자기 자신으로 초기화
    for i in range(1, nlen + 1):
        parent[i] = i

    for edge in adjList:
        cost, a, b = edge
        # 사이클이 발생하지 않는 경우에만 집합에 포함(=연결한다.)
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            answer += cost
    return answer