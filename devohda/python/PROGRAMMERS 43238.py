def solution(n, times):
    answer = 0

    times.sort()

    min_time = 0
    max_time = times[-1] * n

    while min_time <= max_time:
        mid = int((min_time + max_time) / 2)
        wait = 0

        for i in range(len(times)):
            wait += int(mid / times[i])
        if wait < n:
            min_time = mid + 1
        else:
            max_time = mid - 1
            answer = mid

    return answer
