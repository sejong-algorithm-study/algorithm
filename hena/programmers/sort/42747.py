def solution(citations):
    answer = 0
    
    # 정렬
    citations.sort()
    # print(citations)
    
    # 배열 길이
    length = len(citations)
    for i in range(length):
        value = citations[i]
        hindex = length - i
        print(value, hindex)
        if value >= hindex:
            answer = hindex
            break
    return answer