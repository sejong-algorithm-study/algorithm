from collections import deque
    

def solution(begin, target, words):
    answer = 0
    
    queue = deque([begin])
    # print(queue)
    length = len(words)
    visited = [False] * length
    
    while len(queue) > 0:
        q_length = len(queue)
        for _ in range(q_length):
            value = queue.popleft()
            # print("value=",value)
            if value == target:
                return answer

            for i in range(length):
                # print("word=",words[i], end=" ")
                if not visited[i]:
                    cnt = 0
                    for j in range(len(words[i])):
                        if value[j] != words[i][j]:
                            cnt += 1
                    # print("cnt=",cnt)
                    if cnt == 1:
                        visited[i] = True
                        queue.append(words[i])
            # print(queue, visited)
        answer += 1
                
    #             cnt = 0
    #             word_length = len(words[i])
    #             for j in range(word_length):
    #                 if begin[j] == words[i][j]:
    #                     cnt += 1
    #             if cnt == len(words[i]) - 1:
    #                 array.append(words[i])
    #     print("array-in:",array)
    #     while array != []:
    #         value = array.pop()
    #         visited = [False] * len(words)
    #         for i in range(length):
    #             if words[i] == value:
    #                 visited[i] = True
    #         # print(visited)
    #         BFS(value, target, words, length, visited)
    
    return 0