def solution(n, times):
    mintime = 1
    maxtime = times[-1]*n
    while mintime<=maxtime:
        finishtime = (mintime+maxtime)//2
        total_n = 0
        for j in times:
            total_n+=finishtime//j # finishtime동안 심사 가능한 인원을 셈

        if total_n>=n: #만약 심사 가능한 인원이 심사해야 하는 인원보다 많다면
            maxtime = finishtime -1
        else:
            mintime = finishtime+1
    answer = mintime
    return answer
