import heapq
import sys
input = sys.stdin.readline

N = int(input())
classes = [list(map(int, input().split())) for _ in range(N)]

classes.sort()

rooms = [classes[0][1]]
for i in range(1, N):
    st, ed = classes[i]
    if rooms[0] <= st:
        heapq.heappop(rooms)

    heapq.heappush(rooms, ed)

print(len(rooms))
