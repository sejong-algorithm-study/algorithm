from operator import itemgetter
from collections import Counter

r, c, k = map(int, input().split())
# 인덱스는 1부터 시작하므로 맞춰주기 위해 1 빼주기
r -= 1
c -= 1

# 최대 크기가 100이므로 100*100 배열 만들기
A = [[0 for _ in range(100)] for _ in range(100)]
# A 입력 받기
for i in range(3):
    tmp = list(map(int, input().split()))
    for j in range(3):
        A[i][j] = tmp[j]

cnt = 0
row_len = 3
col_len = 3


def R():
    new_col_len = 0
    for i in range(row_len):
        dic = {}
        for j in range(col_len):
            if A[i][j] in dic:
                dic[A[i][j]] += 1
            else:
                dic[A[i][j]] = 1

        dic.pop(0, None)
        list_dic = list(zip(dic.keys(), dic.values()))
        list_dic = sorted(list_dic, key=itemgetter(1, 0))

        idx = 0
        for x, y in list_dic:
            if idx == 100:
                break
            A[i][idx] = x
            idx += 1
            A[i][idx] = y
            idx += 1

        if new_col_len < idx:
            new_col_len = idx

        # 나머지 0으로 초기화
        while idx < col_len:
            A[i][idx] = 0
            idx += 1

    return new_col_len


def C():
    new_row_len = 0
    for j in range(col_len):
        dic = {}
        for i in range(row_len):
            if A[i][j] in dic:
                dic[A[i][j]] += 1
            else:
                dic[A[i][j]] = 1

        dic.pop(0, None)
        list_dic = list(zip(dic.keys(), dic.values()))
        list_dic = sorted(list_dic, key=itemgetter(1, 0))

        idx = 0
        for x, y in list_dic:
            if idx == 100:
                break
            A[idx][j] = x
            idx += 1
            A[idx][j] = y
            idx += 1

        if new_row_len < idx:
            new_row_len = idx

        # 나머지 0으로 초기화
        while idx < row_len:
            A[idx][j] = 0
            idx += 1

    return new_row_len


while True:
    # 100초가 지나도 A[r][c] = k 가 되지 않을 때
    if cnt > 100:
        cnt = -1
        break

    if A[r][c] == k:
        break

    cnt += 1
    if row_len >= col_len:
        col_len = R()
    else:
        row_len = C()

print(cnt)