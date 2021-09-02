import math

# 소수 판별 함수
def is_prime_number(x):
    if x == 0 or x == 1:
        return False
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임


def isPrime(number, arr, primeSet):
    if len(arr) == 0:
        return
    else:
        for i in range(len(arr)):
            numstr = number
            numstr += arr[i]
            popArr = arr.copy()
            if is_prime_number(int(numstr)):
                primeSet.append(int(numstr))
            popArr.pop(i)
            isPrime(numstr, popArr, primeSet)


def solution(numbers):
    numberArr = list(numbers)
    primeArr = []
    isPrime("", numberArr, primeArr)

    print(set(primeArr))
    return len(set(primeArr))