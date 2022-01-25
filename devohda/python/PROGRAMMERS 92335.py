import math


def change_num(num, n):
    new_num = ""
    while num >= n:
        new_num += str(num % n)
        num = num // n
    new_num += str(num)

    return new_num[::-1]


def is_prime(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)), 2):
        if n % i == 0:
            return False

    return True


def solution(n, k):
    nums = change_num(n, k).split('0')

    answer = 0
    for num in nums:
        if num and is_prime(int(num)):
            answer += 1

    return answer

print(solution(9, 10))