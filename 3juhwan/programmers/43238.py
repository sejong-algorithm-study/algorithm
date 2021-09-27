def solution(n, times):
    answer = 0
    start, end = 0, max(times) * n

    while start <= end:
        mid = (start + end) // 2
        people = sum([mid // t for t in times])

        if people >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer