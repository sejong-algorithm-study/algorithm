def solution(citations):
    cnt = [0] * 10001
    for citation in citations:
        cnt[citation] += 1
    
    paper = 0
    for i in range(10000, -1, -1):
        paper += cnt[i]
        if i <= paper:
            return i