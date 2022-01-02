N, K = map(int, input().split())
children = list(map(int, input().split()))

diff = []
for i in range(N - 1):
    diff.append(children[i + 1] - children[i])

diff.sort()
answer = 0

for i in range(N-K):
    answer += diff[i]

print(answer)
