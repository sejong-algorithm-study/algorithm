import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    score = [0 for _ in range(N)]
    cnt = 1
    for _ in range(N):
        a, b = map(int, input().split())
        score[a-1] = b

    min_score = score[0]
    for i in range(1, N):
        if score[i] < min_score:
            cnt += 1
            min_score = score[i]

    print(cnt)
