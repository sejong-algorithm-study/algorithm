import sys
from collections import deque

n = int(sys.stdin.readline())


def D(num):
    return num * 2 if num * 2 <= 9999 else (num * 2) % 10000


def S(num):
    return num - 1 if num != 0 else 9999


def L(num):
    d1 = (num // 100) % 10
    d2 = (num // 10) % 10
    d3 = num % 10
    d4 = num // 1000
    return d1 * 1000 + d2 * 100 + d3 * 10 + d4


def R(num):
    d1 = num % 10
    d2 = num // 1000
    d3 = (num // 100) % 10
    d4 = (num // 10) % 10
    return d1 * 1000 + d2 * 100 + d3 * 10 + d4


for i in range(n):
    A, B = map(int, sys.stdin.readline().split())
    visited = [0] * 10000
    visited[A] = 1
    que = deque([[A, '']])
    while que:
        newA, path = que.popleft()
        DA = D(newA)
        if DA == B:
            print(path + 'D')
            break
        SA = S(newA)
        if SA == B:
            print(path + 'S')
            break
        LA = L(newA)
        if LA == B:
            print(path + 'L')
            break
        RA = R(newA)
        if RA == B:
            print(path + 'R')
            break
        if visited[DA] == 0:
            visited[DA] = 1
            que.append([DA, path + 'D'])
        if visited[SA] == 0:
            visited[SA] = 1
            que.append([SA, path + 'S'])
        if visited[LA] == 0:
            visited[LA] = 1
            que.append([LA, path + 'L'])
        if visited[RA] == 0:
            visited[RA] = 1
            que.append([RA, path + 'R'])
