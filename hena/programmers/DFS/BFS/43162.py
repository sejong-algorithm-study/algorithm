def DFS(n, computers, visited, i, j):
    for index in range(n):
        if computers[j][index] == 1 and visited[index] == 0:
            visited[index] = i + 1
            DFS(n, computers, visited, i, index)

def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and visited[j] == 0:
                DFS(n, computers, visited, i, j)
                
    print(visited)
    arr = [0] * n
    for i in visited:
        arr[i - 1] = 1
    answer = sum(arr)
    
#     for i in range(n):
#         for j in range(n):
#             if computers[i][j] == 1 and visited[j] == False:
#                 visited[j] = i
#                 print(i)
#                 arr[i] = 1
                
#     print(arr)
#     print(visited)
#     answer = sum(arr)
    return answer