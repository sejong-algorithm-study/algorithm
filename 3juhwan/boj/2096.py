import sys
input = sys.stdin.readline

N = int(input())

graph = list(map(int, input().split()))
minDP = graph
maxDP = graph

for i in range(N - 1):
    graph = list(map(int, input().split()))
    tmp1, tmp2 = [0] * 3, [0] * 3
    tmp1[0] = graph[0] + max(maxDP[0], maxDP[1])
    tmp1[1] = graph[1] + max(maxDP[0], maxDP[1], maxDP[2])
    tmp1[2] = graph[2] + max(maxDP[1], maxDP[2])
    maxDP = tmp1
    tmp2[0] = graph[0] + min(minDP[0], minDP[1])
    tmp2[1] = graph[1] + min(minDP[0], minDP[1], minDP[2])
    tmp2[2] = graph[2] + min(minDP[1], minDP[2])
    minDP = tmp2

print(max(maxDP), min(minDP))