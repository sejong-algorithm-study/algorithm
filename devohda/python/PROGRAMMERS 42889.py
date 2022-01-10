def solution(N, stages):
    stages.sort(reverse=True)

    non_clear = [0 for _ in range(N)]
    for stage in stages:
        non_clear[stage - 1] += 1

    clear = [0 for _ in range(N)]
    pointer = 0
    total = 0

    for i in range(N - 1, -1, -1):
        while pointer < len(stages) and i >= stages[pointer]:
            total += 1
            pointer += 1
        clear[i] = total - 1

    print(clear)

    answer = []
    return answer
