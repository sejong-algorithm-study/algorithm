import heapq

N = int(input())
classes = []
for _ in range(N):
    classes.append(list(map(int, input().split())))

classes.sort()
rooms = []

for i in range(len(classes)):
    st, ed = classes[i]
    new_room = True

    if rooms:
        if rooms[0] <= st:
            heapq.heappop(rooms)

    heapq.heappush(rooms, ed)

print(len(rooms))
