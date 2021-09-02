import math
from itertools import permutations


def isPrimeNum(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    arr = set()

    for i in range(1, len(numbers) + 1):
        arr |= set(map(int, map("".join, permutations(numbers, i))))

    for number in arr:
        answer += isPrimeNum(number)

    return answer