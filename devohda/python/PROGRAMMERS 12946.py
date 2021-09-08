def hanoi_tower(start, sub, target, height, move):
    # 하나 작은 탑을 sub 에 만든다.
    # 마지막 남은 거 하나를 target에 옮긴다.
    # 다시 하나 작은 탑을 target에 만든다.

    if height == 0:
        return

    hanoi_tower(start, target, sub, height - 1, move)
    move.append([start, target])
    hanoi_tower(sub, start, target, height - 1, move)


def solution(n):
    answer = []
    hanoi_tower(1, 2, 3, n, answer)
    return answer
