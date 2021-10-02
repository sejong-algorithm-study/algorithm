import sys
import heapq

v, e = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline()) - 1

INF = sys.maxsize
arr = [[] for _ in range(v)]

for i in range(e):
    v1, v2, weight = map(int, sys.stdin.readline().split())
    arr[v1 - 1].append([v2 - 1, weight])


def Dijkstra(start):
    dist = [INF] * v

    dist[start] = 0
    que = []
    heapq.heappush(que, [0, start])

    while que:
        distance, current = heapq.heappop(que)

        for v2, weight in arr[current]:
            newdist = weight + distance
            if newdist < dist[v2]:
                dist[v2] = newdist
                heapq.heappush(que, [newdist, v2])

    return dist

dist = Dijkstra(start)
for i in range(v):
    print(dist[i] if dist[i] != INF else "INF")
