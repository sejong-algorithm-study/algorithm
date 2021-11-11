from collections import deque


def cal_D(n):
    return (n * 2) % 10000


def cal_S(n):
    return n - 1 if n > 0 else 9999


def cal_L(n):
    d1 = n // 1000
    return n % 1000 * 10 + d1


def cal_R(n):
    d4 = n % 10
    return 1000 * d4 + n // 10


def check(n):
    if visited[n]:
        return False
    return True


def bfs():
    A, B = map(int, input().split())
    # A -> B 가 되어야 함
    q = deque([(A, "")])
    visited[A] = 1

    while len(q):
        num, operate = q.popleft()

        if num == B:
            return operate

        num_d = cal_D(num)
        num_s = cal_S(num)
        num_l = cal_L(num)
        num_r = cal_R(num)

        if check(num_d):
            q.append((num_d, operate + 'D'))
            visited[num_d] = 1
        if check(num_s):
            q.append((num_s, operate + 'S'))
            visited[num_s] = 1
        if check(num_l):
            q.append((num_l, operate + 'L'))
            visited[num_l] = 1
        if check(num_r):
            q.append((num_r, operate + 'R'))
            visited[num_r] = 1

    return ""


# T 번 수행
T = int(input())

for _ in range(T):
    visited = [0 for _ in range(10000)]
    print(bfs())
