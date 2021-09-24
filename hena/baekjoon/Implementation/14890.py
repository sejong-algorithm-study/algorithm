import sys
input = sys.stdin.readline
N, L = map(int, input().split())
Map = []
for _ in range(N):
    Map.append(list(map(int, input().split())))
count = 0


def rowDown(arr,row, b, value):
    if b + L >= N:
        return False
    for i in range(b + 1, b + L + 1):
        if arr[i] != value - 1:
            return False
        row[i] = True
    return True

def rowUp(arr, row, b, value):
    if b - L + 1 < 0:
        return False
    if value + 1 != arr[b + 1]:
        return False
    for i in range(b, b - L, -1):
        if arr[i] != value or row[i]:
            return False
        row[i] = True
    return True

def check(A, B):
    if A == B:
        return "same"
    elif A > B:
        return "down"
    else:
        return "up"

def confirm(arr):
    global count
    
    test = [False] * N
    j = 0
    while j < N - 1:
        value = arr[j]
        now = check(arr[j], arr[j + 1])
        if now == 'down':
            if not rowDown(arr, test, j, value):
                break
            j += L
        elif now == 'up':
            if not rowUp(arr, test, j, value):
                break
            j += 1
        else:
            j += 1
    if j == N - 1:
        count += 1

for i in Map:
    confirm(i)
for i in range(N):
    tmp = []
    for j in range(N):
        tmp.append(Map[j][i])
    confirm(tmp)
print(count)