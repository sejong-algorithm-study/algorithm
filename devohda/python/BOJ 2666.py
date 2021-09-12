from collections import deque

n = int(input())  # 벽장 개수
open = list(map(int, input().split()))  # 열린 벽장

m = int(input())  # 이동 횟수
cnt = 0


def cnt_distance(open_door, target_door):
    a, b = open_door
    target = target_door.popleft()

    if len(target_door) == 0:
        return min(abs(target - a), abs(target - b))

    r1 = cnt_distance([target, b], deque(target_door))
    r2 = cnt_distance([target, a], deque(target_door))
    return min(abs(target - a) + r1, abs(target - b) + r2)


cupboard = deque([])
for _ in range(m):
    cupboard.append(int(input()))

cnt = cnt_distance(open, cupboard)
print(cnt)
