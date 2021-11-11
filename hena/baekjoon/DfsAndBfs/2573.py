import sys
from collections import deque

# 입력
input = sys.stdin.readline
N, M = map(int, input().split())

# 그래프 설정
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
# print(board)


# 방향
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

#주변 물 갯수 얻기
def get_water(i, j):
    cnt = 0
    # 4방향 확인
    for direction in range(4):
        nx = i + dx[direction]
        ny = j + dy[direction]
        # 범위 초과 시 무시
        if nx < 0 or nx > N or ny < 0 or ny > M:
            continue
        # 0 = 물이면 갯수 증가
        if not graph[nx][ny]:
            cnt += 1
    return (cnt)

# 몇 개로 이뤄져있는지 확인하기
def BFS(col, row, visited):
    
    queue = deque([(col, row)])
    # 이어져있는 것들 전부 바꿔줌
    while queue:
        i, j = queue.popleft()
        for direction in range(4):
            nx = i + dx[direction]
            ny = j + dy[direction]
            if nx < 0 or nx > N or ny < 0 or ny > M:
                continue
            if not visited[nx][ny] and graph[nx][ny] > 0:
                visited[nx][ny] = True
                queue.append((nx, ny))
                
stack = []
break_cnt = 0
while True:
    total_cnt = 0
    
    visited = [[False] * M for _ in range(N)]
    # Brute-Force로 전부 확인
    for i in range(N):
        for j in range(M):
            # 높이가 1이상의 빙하 찾기
            if graph[i][j] > 0:
                #줄어들 높이 얻고 위치+높이 넣기
                cnt = get_water(i, j)
                stack.append( (i, j, cnt) )
                # 방문하지 않았다면 방문처리 후 조각 갯수 증가
                if not visited[i][j]:
                    BFS(i, j, visited)
                    total_cnt += 1

    # 조각 갯수가 2 이상이면 펑
    if total_cnt > 1:
        # print(total_cnt)
        print(break_cnt)
        exit()
    
    # 스택 정보의 좌표에 높이만큼 빼주기
    while stack:
        col, row, cnt = stack.pop()
        if graph[col][row] < cnt:
            graph[col][row] = 0
        else:    
            graph[col][row] -= cnt
            # and not visited[i][j]:
    # print("start")
    # for i in range(N):
    #     for j in range(M):
    #         print(board[i][j],end="")
    #     print()
    # print("end")
    
    # 야매인데 어케 고쳐야 할까....... 마음에 안드는 코드 남에꺼 참고하기
    if visited == [[False]*M for _ in range(N)]:
        break
    # 한바퀴 돌면 횟수가 돌음
    break_cnt += 1
print(0)
    # for i in range(N):
    #     for j in range(M):
    #         if board[i][j] > 0:
                
    
        


