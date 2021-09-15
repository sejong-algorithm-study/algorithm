import sys
from itertools import chain, combinations

input = sys.stdin.readline
N, time = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
score=0
for i in range(N,0,-1):
    for j in combinations(arr,i):
        if sum(list(zip(*j))[0]) <=310:
            a=sum(list(zip(*j))[1])
            if score < a:
                score=a
print(score)