from collections import defaultdict
from collections import deque

confetti = [
    [],
    [[0], [0]],
    [[0, 1], [0, 1]],
    [[0, 1, 2], [0, 1, 2]],
    [[0, 1, 2, 3], [0, 1, 2, 3]],
    [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
]

cover = defaultdict(list)
# 종이 입력 받기
paper = []
for i in range(10):
    paper.append(list(map(int, input().split())))
    for j in range(10):
        if paper[i][j] == 1:
            cover[i].append(j)

answer = -1
q = deque([(paper, cover, [0, 0, 0, 0, 0])])


print(answer)
