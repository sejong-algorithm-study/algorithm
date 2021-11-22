# 배열 크기
n = int(input())
A = []
B = []
C = []
D = []
for _ in range(n):
    a, b, c, d = list(map(int, input().split()))
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

A.sort()
B.sort()
C.sort()
D.sort()

visited = [[[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
answer = []


def add_if_bigger(s1, e1, s2, e2, s3, e3, s4, e4, m1, m2, m3, m4):
    is_zero(s1, m1 - 1, s2, e2, s3, e3, s4, e4)
    is_zero(s1, e1, s2, m2 - 1, s3, e3, s4, e4)
    is_zero(s1, e1, s2, e2, s3, m3 - 1, s4, e4)
    is_zero(s1, e1, s2, e2, s3, e3, s4, m4 - 1)
    visited[(s1 + m1 - 1) // 2][(s2 + e2) // 2][(s3 + e3) // 2][(s4 + e4) // 2] = 1
    visited[(s1 + e1) // 2][(s2 + m2 - 1) // 2][(s3 + e3) // 2][(s4 + e4) // 2] = 1
    visited[(s1 + e1) // 2][(s2 + e2) // 2][(s3 + m3 - 1) // 2][(s4 + e4) // 2] = 1
    visited[(s1 + e1) // 2][(s2 + e2) // 2][(s3 + e3) // 2][(s4 + m4 - 1) // 2] = 1


def add_if_smaller(s1, e1, s2, e2, s3, e3, s4, e4, m1, m2, m3, m4):
    is_zero(m1 + 1, e1, s2, e2, s3, e3, s4, e4)
    is_zero(s1, e1, m2 + 1, e2, s3, e3, s4, e4)
    is_zero(s1, e1, s2, e2, m3 + 1, e3, s4, e4)
    is_zero(s1, e1, s2, e2, s3, e3, m4 + 1, e4)
    visited[(e1 + m1 + 1) // 2][(s2 + e2) // 2][(s3 + e3) // 2][(s4 + e4) // 2] = 1
    visited[(s1 + e1) // 2][(e2 + m2 + 1) // 2][(s3 + e3) // 2][(s4 + e4) // 2] = 1
    visited[(s1 + e1) // 2][(s2 + e2) // 2][(e3 + m3 + 1) // 2][(s4 + e4) // 2] = 1
    visited[(s1 + e1) // 2][(s2 + e2) // 2][(s3 + e3) // 2][(e4 + m4 + 1) // 2] = 1


def is_zero(s1, e1, s2, e2, s3, e3, s4, e4):
    if s1 > e1 or s2 > e2 or s3 > e3 or s4 > e4:
        return 0

    m1 = (s1 + e1) // 2
    m2 = (s2 + e2) // 2
    m3 = (s3 + e3) // 2
    m4 = (s4 + e4) // 2

    if visited[m1][m2][m3][m4] == 1:
        return 0

    add_val = A[m1] + B[m2] + C[m3] + D[m4]
    visited[m1][m2][m3][m4] = 1
    if add_val == 0:
        answer.append((m1, m2, m3, m4))
        add_if_bigger(s1, e1, s2, e2, s3, e3, s4, e4, m1, m2, m3, m4)
        add_if_smaller(s1, e1, s2, e2, s3, e3, s4, e4, m1, m2, m3, m4)
        return

    if add_val > 0:
        add_if_bigger(s1, e1, s2, e2, s3, e3, s4, e4, m1, m2, m3, m4)
        return
    else:
        add_if_smaller(s1, e1, s2, e2, s3, e3, s4, e4, m1, m2, m3, m4)
        return


is_zero(0, n - 1, 0, n - 1, 0, n - 1, 0, n - 1)
print(len(list(set(answer))))
