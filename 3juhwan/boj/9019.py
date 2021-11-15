from collections import deque
import sys
input = sys.stdin.readline

def convert(x):
    return (x+10000)%10000

def run(i, x):
    if i == 0:
        return convert(2*x)
    if i == 1:
        return convert(x-1)
    if i == 2:
        return x%1000*10+x//1000
    if i == 3:
        return x%10*1000+x//10

n = int(input())
for __ in range(n):
    s, e = map(int, input().split())
    visited = [''] * 10000
    command = 'DSLR'
    q = deque([s])
    while q:
        x = q.popleft()

        if x == e:
            print(visited[x])
            break
        
        s = visited[x]
        for i in range(4):
            r = run(i, x)
            if visited[r] == '':
                visited[r] = s + command[i]
                q.append(r)