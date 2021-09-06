def recursive(numbers, Sum, index, length, target):
    # print(Sum)
    if length == index:
        if Sum == target:
            return (1)
        else:
            return (0)
    return recursive(numbers, Sum + numbers[index], index + 1, length, target) + recursive(numbers, Sum - numbers[index], index + 1, length, target)

def solution(numbers, target):
    answer = 0
    length = len(numbers)
    answer = recursive(numbers, 0, 0, length, target)
    return answer