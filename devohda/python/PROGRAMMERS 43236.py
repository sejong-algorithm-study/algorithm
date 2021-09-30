from collections import deque


def solution(distance, rocks, n):
    answer = distance

    rocks.sort()
    rocks.append(distance)

    # 거리 저장
    space = deque([rocks[0]])
    for i in range(1, len(rocks)):
        space.append(rocks[i] - rocks[i - 1])

    min_distance = 1
    max_distance = distance

    while min_distance <= max_distance:
        cnt = 0
        mid = int((max_distance + min_distance) / 2)
        copy_space = space.copy()

        change_space = []
        s = copy_space.popleft()
        if s <= mid:
            cnt += 1
            rs = copy_space.popleft()
            change_space.append(s + rs)
        else:
            change_space.append(s)

        while len(copy_space) != 0:
            s = copy_space.popleft()
            last_insert = change_space.pop()
            if last_insert <= mid:
                cnt += 1
                change_space.append(last_insert + s)
            else:
                change_space.append(last_insert)
                if s <= mid:
                    if len(copy_space) == 0:
                        change_space.append(s)
                    else:
                        cnt += 1
                        rs = copy_space.popleft()
                        change_space.append(s + rs)
                else:
                    change_space.append(s)

        if cnt > n:
            max_distance = mid - 1
        else:
            min_distance = mid + 1
            answer = min(change_space)

    return answer
