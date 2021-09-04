def getTargetNum(numbers, target, i, sum):
    if i == len(numbers):
        if sum == target:
            return 1
        return 0
    return getTargetNum(numbers, target, i+1, sum+numbers[i]) + getTargetNum(numbers, target, i+1, sum-numbers[i])
    
def solution(numbers, target):
    return getTargetNum(numbers, target, 0, 0)