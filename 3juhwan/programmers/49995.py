def solution(cookie):
    answer = 0
    cookie = [0]+cookie+[0]
    for i in range(1, len(cookie)-1):
        left, right = i, i+1
        leftSum, rightSum = cookie[left], cookie[right]
        while left > 0 and right < len(cookie)-1:
            if leftSum == rightSum:
                answer = max(answer, leftSum)
                left, right = left-1, right+1
                leftSum += cookie[left]
                rightSum += cookie[right]
            elif leftSum > rightSum:
                right += 1
                rightSum += cookie[right]
            elif leftSum < rightSum:
                left -= 1
                leftSum += cookie[left]
    
    return answer