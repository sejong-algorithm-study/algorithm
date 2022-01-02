import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
crains = list(map(int, input().split()))
crains.sort(reverse=True)

M = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)

if crains[0] < boxes[0]:
    print(-1)
else:
    shifted = 0
    minutes = 0

    while shifted < M:
        minutes += 1
        for crain in crains:
            for k in range(shifted, M):
                if crain >= boxes[k]:
                    shifted += 1
                    break
    print(minutes)