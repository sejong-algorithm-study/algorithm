from math import ceil
def solution(n, stations, w):
    answer=0
    start = 1 #시작 지점
    for i in stations:
        answer += ceil((i-w-start)/(2*w+1))
        start = i+w+1
    if start<=n:
        answer +=ceil((n-start+1)/(2*w+1))
    return answer