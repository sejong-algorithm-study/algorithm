def solution(distance, rocks, n):
    answer = 0
    rocks = sorted(rocks) + [distance]

    start, end = 0, distance
    while start <= end:
        mid = (start + end) // 2        
        s, cnt = [0] * 2
        for rock in rocks:
            if rock - s < mid:
                cnt += 1
            else:
                s = rock

        # 방문한 바위 갯수가 한계보다 작다면, 
        if cnt <= n:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer