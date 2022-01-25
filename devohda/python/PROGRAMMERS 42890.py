from itertools import combinations


def solution(relation):
    length = len(relation[0])
    type = len(relation)
    info = [[] for _ in range(length)]
    for r in relation:
        for i in range(length):
            info[i].append(r[i])

    answer = 0

    select = 0
    idx = set(range(length))

    while select < len(idx):
        select += 1
        n_idx = idx
        for comb in list(combinations(idx, select)):
            tuples = []
            for i in range(type):
                tmp = []
                for c in comb:
                    tmp.append(info[c][i])
                tuples.append(tuple(tmp))

            if len(tuples) == len(set(tuples)):
                n_idx = n_idx - set(comb)
                answer += 1
        idx = n_idx

    return answer


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
