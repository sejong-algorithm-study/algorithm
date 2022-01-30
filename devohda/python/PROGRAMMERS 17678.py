from collections import deque


def solution(n, t, m, timetable):
    crews = []
    for time in timetable:
        hour, min = list(map(int, time.split(':')))
        crews.append(hour * 60 + min)

    crews.sort()
    crews = deque(crews)

    # 이전 버스들 운행시키기
    start_t = 9 * 60
    for i in range(n - 1):
        bus = 0
        while bus < m:
            if crews[0] <= start_t:
                crews.popleft()
                bus += 1
            else:
                break
        start_t += t

    last_bus = start_t
    last_crew = 0
    bus = 0

    while crews and bus < m:
        if crews[0] <= last_bus:
            last_crew = crews.popleft()
            bus += 1
        else:
            break

    if crews and crews[0] > last_bus:
        crews = []

    last_crew -= 1
    if not crews and bus < m:
        return str(last_bus // 60).zfill(2) + ':' + str(last_bus % 60).zfill(2)
    else:
        return str(last_crew // 60).zfill(2) + ':' + str(last_crew % 60).zfill(2)


print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
