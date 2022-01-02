import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

sensor = list(map(int, input().split()))
sensor.sort()

dist = []
for i in range(N - 1):
    dist.append(sensor[i + 1] - sensor[i])

dist.sort()

answer = 0
for i in range(N - K):
    answer += dist[i]

print(answer)
