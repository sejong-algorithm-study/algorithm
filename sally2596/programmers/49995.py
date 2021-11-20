def solution(cookie):
    answer = -1
    n = len(cookie)
    for i in range(1, n ):
        l = i - 1
        r = i
        sum1 = cookie[l]
        sum2 = cookie[r]
        while l>=0 and r<n:
            if sum1 == sum2:
                answer = max(answer, sum1)
            if l>0 and sum1<=sum2:
                l-=1
                sum1 += cookie[l]
            elif r+1<n and sum2<=sum1:
                r+=1
                sum2 += cookie[r]
            else:
                break

    if answer<=0:
        answer = 0
    return answer
print(solution([1,1,2,3]))