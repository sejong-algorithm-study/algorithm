dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(place, visited, x, y, cnt):    
    ret = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and not place[nx][ny] == 'X':
            if place[nx][ny] == 'P':
                if cnt <= 1:
                    return 1
                return 0
            visited[nx][ny] = 1
            ret += dfs(place, visited, nx, ny, cnt+1)
    return ret


def isSafety(place):
    visited = [[0]*5 for __ in range(5)]
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                visited[i][j] = 1
                if dfs(place, visited, i, j, 0):
                    return 0  
    return 1    


def solution(places):
    answer = []
    for place in places:
        answer.append(isSafety(place))
    return answer