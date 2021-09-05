from collections import deque


def solution(begin, target, words):
    visited = [False] * len(words)
    queue = deque([(begin, 0)])

    while queue:
        word, cnt = queue.popleft()

        if word == target:
            return cnt

        for i in range(len(words)):
            difference = 0

            if visited[i]:
                continue

            for a, b in zip(word, words[i]):
                if a != b:
                    difference += 1
            if difference == 1:
                visited[i] = True
                queue.append((words[i], cnt + 1))

    return 0