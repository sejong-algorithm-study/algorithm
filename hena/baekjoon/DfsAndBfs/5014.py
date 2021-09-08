# G5 5014 스타트링크
# 시간 제한: 1초
# 메모리 제한 256MB
# link: https://www.acmicpc.net/problem/5014

import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())

#F 총 층수
#S 강호의 현 위치
#G 스타트링크 위치
#U 업 D 다운

queue = deque([(S,0)])
# print(queue)
visited = [False] * (F + 1)
visited[S] = True

while queue:
    value, cnt = queue.popleft()
    
    # print(value, end=" ")
    
    if value == G:
        print(cnt)
        exit()
    cnt += 1
    Up = value + U
    Down = value - D
    if Up <= F and not visited[Up]:
        queue.append((Up, cnt))
        visited[Up] = True
    if Down >= 1 and not visited[Down]:
        queue.append((Down, cnt))
        visited[Down] = True

print("use the stairs")


# comment:
# queue에서 pop한 값으로 방문 처리 시 더 많은 경우를 봐야하므로 시간이 오래 걸린다.