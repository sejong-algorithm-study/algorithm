from collections import deque

def canConvert(word, comp):
    n = [1 for w, c in zip(word, comp) if w != c]
    return True if len(n) == 1 else False

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = [0] * (len(words))
    stack = deque([(begin, 0)])
    
    while stack:
        now, cnt = stack.popleft()
        
        if now == target:
            return cnt
        
        for i in range(len(words)):
            if not visited[i] and canConvert(now, words[i]):
                stack.append((words[i], cnt+1))
                visited[i] = 1