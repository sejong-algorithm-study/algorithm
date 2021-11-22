import heapq


def time_to_num(time):
    arr = time.split(':')
    return float(arr[0]) * 3600 + float(arr[1]) * 60 + float(arr[2])


def solution(lines):
    answer = 0
    q = []
    heapq.heapify(q)
    for line in lines:
        info = line.split()
        end_time = time_to_num(info[1])
        start_time = end_time - float(info[2][:-1]) + 0.001
        heapq.heappush(q, (start_time, end_time))

    q2 = []
    heapq.heapify(q2)
    while q:
        st, et = heapq.heappop(q)
        heapq.heappush(q2, (et, st))

        while q2[0][0] <= st - 1:
            heapq.heappop(q2)

        if len(q2) > answer:
            answer = len(q2)

    return answer