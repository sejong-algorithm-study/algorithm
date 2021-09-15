import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    N = int(input())
    arr = []
    for i in range(N):
        A, B = map(int, input().split())
        arr.append([A, B])
    arr.sort(key = lambda x: (x[0]))
    
    # print(arr)
    
    count = 1
    init = arr[0][1]
    for i in range(1, N):
        if init > arr[i][1]:
            init = arr[i][1]
            count += 1
    print(count)